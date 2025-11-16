import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "products.json")

def load_products():
    """Carrega os produtos e seletores do JSON."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["products"]