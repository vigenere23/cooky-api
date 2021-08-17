from dotenv import load_dotenv
load_dotenv()

import os
from envyaml import EnvYAML

environment = os.getenv('ENVIRONMENT', 'local')
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, '..', f'config.{environment}.yml')
config = EnvYAML(path)
