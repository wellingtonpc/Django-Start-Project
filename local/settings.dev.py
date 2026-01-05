RUN_TYPE = """⚠️  > DEVELOPMENT MODE <  ⚠️\n"""

DEBUG = True
SECRET_KEY = 'django-insecure-4@&rcqdi9_=^0)!g=kerygx5po33q^ux+oqot&sb1+s(5anit)'

LOGGING['formatters']['colored'] = {  # type: ignore # noqa F821
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}

LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore # noqa F821
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore # noqa F821
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore # noqa F821
