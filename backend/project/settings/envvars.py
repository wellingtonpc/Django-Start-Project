from core.utils.collections import deep_update
from core.utils.settings import get_settings_from_environment

"""
This takes any variable with a matching prefix, strips out the prefix, 
and adds it to global

Example:
export CORESETTINGS_IN_DOCKER=true (environment variable)

Could then be referenced in setting as:
IN_DOCKER = True
"""

# globals() is a dictionary of global variables

deep_update(
    globals(),
    get_settings_from_environment(ENVVAR_SETTINGS_PREFIX) # type: ignore
    )