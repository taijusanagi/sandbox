import argparse
import json
import re
import subprocess
from pathlib import Path

BITRATE = "128k"

parser = argparse.ArgumentParser(description="Convert an M4B audiobook to MP3")
parser.add_argument("file", type=Path, help="M4B file to convert")
source = parser.parse_args().file
if not source.is_file():
    parser.error(f"input file not found: {source.resolve()}")

output_root = Path(__file__).resolve().parent / "output"
output_dir = output_root / source.stem
output_dir.mkdir(parents=True, exist_ok=True)

probe = subprocess.run([
    "ffprobe", "-v", "error", "-show_chapters", "-show_format", "-show_streams",
    "-of", "json", str(source),
], capture_output=True, text=True)
if probe.returncode:
    parser.error(f"ffprobe could not read {source}: {probe.stderr.strip()}")
info = json.loads(probe.stdout)
chapters = info.get("chapters", [])
if not chapters:
    parser.error("the input file has no chapter metadata")

cover = next((s["index"] for s in info.get("streams", [])
              if s.get("disposition", {}).get("attached_pic")), None)
total = len(chapters)
for number, chapter in enumerate(chapters, 1):
    title = chapter.get("tags", {}).get("title", f"Chapter {number:02}")
    title = re.sub(r'[\\/:*?"<>|]', "_", title).strip() or f"Chapter {number:02}"
    output = output_dir / f"{number:03} - {title}.mp3"
    start, end = float(chapter["start_time"]), float(chapter["end_time"])
    command = ["ffmpeg", "-y", "-ss", str(start), "-i", str(source),
               "-map", "0:a:0"]
    if cover is not None:
        command += ["-map", f"0:{cover}", "-c:v", "copy", "-disposition:v", "attached_pic"]
    command += ["-t", str(end - start), "-codec:a", "libmp3lame", "-b:a", BITRATE,
                "-map_metadata", "0", "-metadata", f"title={title}",
                "-metadata", f"track={number:02}", "-id3v2_version", "3", str(output)]
    subprocess.run(command, check=True)
