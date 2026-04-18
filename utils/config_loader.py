import yaml
from pathlib import Path
from typing import List, Dict


def load_sites_config() -> List[Dict]:
    config_path = Path(__file__).parent.parent / 'configs' / 'sites.yaml'
    print(config_path)  # Debugging line to check the path
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config['sites']