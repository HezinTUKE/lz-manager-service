from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).resolve().parent / "config.yml"

with open(CONFIG_PATH, "r") as file:
    config_data = yaml.safe_load(file)

config_db = config_data.get("database", {})
