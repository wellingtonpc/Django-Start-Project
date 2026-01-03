# Contributing to Django Start Project

Thank you for your interest in contributing to Django Start Project! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Django-Start-Project.git
   cd Django-Start-Project
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Development Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure they follow the project's coding standards

3. Run tests to make sure everything works:
   ```bash
   pytest
   ```

4. Commit your changes with a descriptive commit message:
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

5. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Open a Pull Request from your fork to the main repository

## Code Style

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused on a single task
- Write comments for complex logic

## Testing

- Write tests for new features and bug fixes
- Ensure all tests pass before submitting a PR
- Aim for good test coverage (we use pytest-cov)
- Run tests with:
  ```bash
  pytest
  ```
- Run tests with coverage:
  ```bash
  pytest --cov=core --cov=config --cov-report=html
  ```

## Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Update documentation if needed
- Add or update tests as necessary
- Ensure all tests pass
- Write a clear PR description explaining your changes
- Reference any related issues

## Reporting Issues

When reporting issues, please include:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

## Feature Requests

We welcome feature requests! Please:
- Check if the feature has already been requested
- Clearly describe the feature and its use case
- Explain why this feature would be useful to most users

## Questions?

If you have questions, feel free to:
- Open an issue with the "question" label
- Check existing issues and pull requests

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
