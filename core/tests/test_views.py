import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestHomeView:
    """Tests for the home view."""
    
    def test_home_view_returns_200(self, client):
        """Test that home view returns a 200 status code."""
        url = reverse('core:home')
        response = client.get(url)
        assert response.status_code == 200
    
    def test_home_view_uses_correct_template(self, client):
        """Test that home view uses the correct template."""
        url = reverse('core:home')
        response = client.get(url)
        assert 'home.html' in [t.name for t in response.templates]
    
    def test_home_view_contains_welcome_text(self, client):
        """Test that home view contains welcome text."""
        url = reverse('core:home')
        response = client.get(url)
        assert b'Welcome to Django Start Project' in response.content


@pytest.mark.django_db
class TestAuthentication:
    """Tests for authentication functionality."""
    
    def test_login_page_accessible(self, client):
        """Test that login page is accessible."""
        url = reverse('account_login')
        response = client.get(url)
        assert response.status_code == 200
    
    def test_signup_page_accessible(self, client):
        """Test that signup page is accessible."""
        url = reverse('account_signup')
        response = client.get(url)
        assert response.status_code == 200
    
    def test_user_can_login(self, client, user):
        """Test that a user can login."""
        url = reverse('account_login')
        response = client.post(url, {
            'login': 'testuser',
            'password': 'testpass123'
        })
        # Should redirect after successful login
        assert response.status_code == 302
