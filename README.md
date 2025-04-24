# ProteinGym2 Project Template

This repo is the cookiecutter template to containerize the model and expose its predict or train interfaces.

## Getting started

1. You can create your project by:

```shell
cookiecutter https://github.com/ProteinGym2/pg2-project.git
```

2. After you've created your project, then you can run:

```shell
docker compose up --build
```

The `sample.csv` will be used for the prediction, and it will generate `output.json` where the predictions are saved for future evaluation.

You can start to include your own model by adding the code in `src` folder.
