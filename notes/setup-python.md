## Policies

- Replicate the Google Colab environment as closely as possible.
- Make the environment disposable.

## Commands

### Create a Conda Environment
```
conda create --name sandbox python=3.13.15 -y
```

### Activate the Environment
```
conda activate sandbox
```

### Install the Packages
```
pip install -r requirements.txt
```

### Deactivate the Environment
```
conda deactivate
```

### Remove the Environment
```
conda remove --name sandbox --all -y
```

### Get Current Environment Information in Colab
```
!python --version
!pip freeze > colab_requirements.txt
```
