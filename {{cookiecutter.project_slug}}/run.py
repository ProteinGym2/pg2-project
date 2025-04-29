#!/usr/local/bin/python

import pandas as pd
import random
import json
from loguru import logger
import typer

app = typer.Typer()

with open("manifest.json") as f:
    config = json.load(f)

@app.command()
def predict(
    input_file: str = "data/sample.csv",
    output_file: str = "data/output.csv"
):

    logger.info(f"Reading from {input_file}")
    logger.info(f"Generating outputs")

    data = pd.read_csv(input_file)
    target = "attr1"
    
    random.seed(config["model"]["params"]["seed"])
    output = {
        "sequence": [v for v in data["sequence"].values],
        "actual": [float(v) for v in data["attr1"].values],
        "predicted": list([random.random() for i in range(data.shape[0])]),
        "split": [v for v in data["split"].values],
    }

    output_df = pd.DataFrame(output)
    output_df.to_csv(output_file)

    logger.info(f"Done. Check {output_file}")


@app.command()
def test():
    pass


if __name__ == "__main__":
    app()
