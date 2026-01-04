import os
from pathlib import Path
from split_settings.tools import optional, include


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Namespacing or own custom environments variables
ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_' 

LOCAL_SETTINGS_PATH = os.getenv(
    f'{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH', 
    BASE_DIR.parent / 'local/settings.dev.py'
)

include(
    'base.py',
    'custom.py',
    optional(LOCAL_SETTINGS_PATH),
    'envvars.py',
    'docker.py',
)