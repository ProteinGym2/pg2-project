import pandas as pd
from random import random
import json

if __name__ == '__main__':
    dataset = "data/sample.csv"
    data = pd.read_csv(dataset)
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
            "dataset": dataset
        }
    }

    with open("data/outputs.json", "w") as file:
        json.dump(output, file)

    
