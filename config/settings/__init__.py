from decouple import config

ENVIRONMENT = config('ENVIRONMENT', None)
if ENVIRONMENT:
    if ENVIRONMENT == "DEV":
        from .development_settings import *
    elif ENVIRONMENT == "STAG":
        from .stagging_settings import *
    elif ENVIRONMENT == "PROD":
        from .production_settings import *