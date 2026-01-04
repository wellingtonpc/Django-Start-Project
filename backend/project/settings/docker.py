if IN_DOCKER:  # type: ignore # noqa: F821
    RUN_TYPE = """⚠️  > DOCKER - DEVELOPMENT MODE <  ⚠️\n"""

    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware'
    ]
