#!/usr/local/bin/python

import pandas as pd
from random import random
import json
from loguru import logger
import typer

app = typer.Typer()

@app.command()
def predict(
    input_file: str = "data/sample.csv",
    output_file: str = "data/output.json"
):

    logger.info(f"Reading from {input_file}")
    logger.info(f"Generating outputs")

    data = pd.read_csv(input_file)
    target = "attr1"
    
    output = {
        "actual": [float(v) for v in data["attr1"].values],
        "predicted": list([random() for i in range(data.shape[0])]),
        "model": {
            "name": "random heuristic",
            "params": {
                "seed": 0
            }
        },
        "metadata": {
            "dataset": input_file
        }
    }

    with open(output_file, "w") as file:
        json.dump(output, file)

    logger.info(f"Done. Check {output_file}")


@app.command()
def test():
    pass


if __name__ == "__main__":
    app()
