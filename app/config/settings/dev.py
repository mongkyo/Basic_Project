from .base import *

dev_secrets = json.load(open(os.path.join(SECRET_ROOT, 'dev.json')))
