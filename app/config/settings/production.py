from .base import *

production_secrets = json.load(open(os.path.join(SECRET_ROOT, 'production.json')))
