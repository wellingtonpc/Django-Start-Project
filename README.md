# Django Start Project 🚀

A production-ready Django template project pre-configured with modern tools and best practices.

## Features ✨

- **Django 5.0+**: Latest Django framework
- **Django Allauth**: Complete authentication system with social login support
- **Pytest**: Modern testing framework with coverage reporting
- **Docker & Docker Compose**: Containerized development environment
- **PostgreSQL**: Production-grade database
- **DaisyUI**: Beautiful UI components built on Tailwind CSS
- **HTMX**: Dynamic frontend interactions without JavaScript
- **WhiteNoise**: Efficient static file serving
- **Environment Variables**: Secure configuration management

## Quick Start 🏃

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/wellingtonpc/Django-Start-Project.git
cd Django-Start-Project
```

2. Copy the environment file:
```bash
cp .env.example .env
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

4. Access the application at `http://localhost:8000`

5. Create a superuser (in a new terminal):
```bash
docker-compose exec web python manage.py createsuperuser
```

### Local Development (Without Docker)

1. Clone the repository:
```bash
git clone https://github.com/wellingtonpc/Django-Start-Project.git
cd Django-Start-Project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the environment file:
```bash
cp .env.example .env
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create static directories:
```bash
mkdir -p static staticfiles
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Access the application at `http://localhost:8000`

## Running Tests 🧪

### With Docker:
```bash
docker-compose exec web pytest
```

### Locally:
```bash
pytest
```

### With coverage report:
```bash
pytest --cov=core --cov=config --cov-report=html
```

View the coverage report by opening `htmlcov/index.html` in your browser.

## Project Structure 📁

```
Django-Start-Project/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── core/                   # Main application
│   ├── tests/             # Application tests
│   ├── views.py           # Views
│   └── urls.py            # App URL configuration
├── templates/              # HTML templates
│   ├── base.html          # Base template with DaisyUI & HTMX
│   ├── home.html          # Home page
│   └── account/           # Allauth templates
├── static/                 # Static files (CSS, JS, images)
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
└── .env.example            # Environment variables example
```

## Environment Variables 🔐

Copy `.env.example` to `.env` and customize the following variables:

- `SECRET_KEY`: Django secret key (change in production!)
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection URL
- `EMAIL_BACKEND`: Email backend configuration
- `DEFAULT_FROM_EMAIL`: Default sender email

## Technologies Used 🛠️

- **Backend**: Django 5.0+
- **Database**: PostgreSQL (SQLite for local development)
- **Authentication**: django-allauth
- **Testing**: pytest, pytest-django, pytest-cov
- **Frontend**: DaisyUI (Tailwind CSS), HTMX, Alpine.js
- **Containerization**: Docker, Docker Compose
- **Static Files**: WhiteNoise

## Features Included 📦

### Authentication
- User registration
- Login/Logout
- Password reset
- Email verification (configurable)
- Social authentication ready

### UI Components
- Responsive navbar with user menu
- Beautiful forms with DaisyUI
- Alert messages
- Modal support
- Dark mode ready

### Development Tools
- Pre-configured pytest
- Coverage reporting
- Docker support
- Environment-based configuration
- Static file handling

## Customization 🎨

### Adding New Apps
```bash
python manage.py startapp myapp
```

Then add to `INSTALLED_APPS` in `config/settings.py`.

### Customizing DaisyUI Theme
Edit the `data-theme` attribute in `templates/base.html`:
```html
<html lang="en" data-theme="dark">
```

Available themes: light, dark, cupcake, bumblebee, emerald, corporate, synthwave, retro, cyberpunk, valentine, halloween, garden, forest, aqua, lofi, pastel, fantasy, wireframe, black, luxury, dracula, cmyk, autumn, business, acid, lemonade, night, coffee, winter

### Adding HTMX Endpoints
Create a view that returns HTML fragments:
```python
def htmx_view(request):
    return render(request, 'fragment.html', context)
```

## Production Deployment 🚀

1. Set `DEBUG=False` in `.env`
2. Generate a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up PostgreSQL database
5. Configure email backend
6. Run `python manage.py collectstatic`
7. Use a production WSGI server (Gunicorn, uWSGI)
8. Set up HTTPS with a reverse proxy (Nginx, Caddy)

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💬

If you have any questions or need help, please open an issue on GitHub.
