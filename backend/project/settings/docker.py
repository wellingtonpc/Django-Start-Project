if IN_DOCKER: #  type: ignore
    RUN_TYPE = """⚠️  > DOCKER - DEVELOPMENT MODE <  ⚠️\n"""

    assert MIDDLEWARE[:1] == [ #  type: ignore
    'django.middleware.security.SecurityMiddleware'
    ]