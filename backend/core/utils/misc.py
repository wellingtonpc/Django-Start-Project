import yaml


def yaml_coerce(value):
    # Convert value to proper Python
    if isinstance(value, str):
        # yaml.load returns a python object
        # converts string dict  "{'key': 'value'}" to python dict {'key': 'value'}
        # Useful because sometimes we need to stringify dicts
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
