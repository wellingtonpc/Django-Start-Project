"""
Custom management command example.

This command creates a sample superuser for development.
Usage: python manage.py create_dev_user
"""
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a development superuser if it does not exist'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin123'

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" already exists.')
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created superuser:\n'
                f'  Username: {username}\n'
                f'  Email: {email}\n'
                f'  Password: {password}\n'
                f'  \n'
                f'  ⚠️  WARNING: This is for development only!'
            )
        )
