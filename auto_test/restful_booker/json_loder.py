import json

def load_schema(path: str):
    with open(path, "r") as file:
        schema = json.load(file)
    return schema