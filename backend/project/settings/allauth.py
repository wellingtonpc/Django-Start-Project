# Application definition

INSTALLED_APPS += [  # type: ignore # noqa F821
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.microsoft',
]


MIDDLEWARE += [  # type: ignore # noqa F821
    'allauth.account.middleware.AccountMiddleware'
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    'microsoft': {
        'APP': {'client_id': 'your-application-client-id', 'secret': 'your-client-secret-value', 'key': ''},
        'SCOPE': ['openid', 'profile', 'email'],
        'AUTH_PARAMS': {'prompt': 'select_account'},
        'TENANT': 'common',  # or your specific tenant ID for company access
    }
}

# Overall
ACCOUNT_FORMS = {
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'confirm_login_code': 'allauth.account.forms.ConfirmLoginCodeForm',
    'login': 'allauth.account.forms.LoginForm',
    'request_login_code': 'allauth.account.forms.RequestLoginCodeForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'signup': 'allauth.account.forms.SignupForm',
    'user_token': 'allauth.account.forms.UserTokenForm',
}

ACCOUNT_SESSION_REMEMBER = False

# Signup
# ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_LOGIN_METHOD = {'email', 'username'}

ACCOUNT_EMAIL_VERIFICATION = 'optional'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
