import pandas as pd
from random import random
import json
from loguru import logger
import click

@click.group()
def cli():
    pass

@cli.command(name="predict", help="predict the targets from the input dataframes")
@click.option("--input-file", help="the input CSV dataframe")
@click.option("--output-file", help="the output JSON predicted targets")
def predict(input_file: str, output_file: str):

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

if __name__ == "__main__":
    cli()
