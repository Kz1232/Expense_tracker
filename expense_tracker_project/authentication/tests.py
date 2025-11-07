from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import LoginForm, SignupForm

User = get_user_model()


class UserModelTests(TestCase):
    """Test User model performance optimizations."""

    def test_user_email_is_indexed(self):
        """Verify that email field has database index."""
        user = User._meta.get_field('email')
        self.assertTrue(user.db_index)

    def test_user_meta_indexes_defined(self):
        """Verify that composite indexes are defined."""
        indexes = User._meta.indexes
        self.assertEqual(len(indexes), 2)
        index_fields = [list(idx.fields) for idx in indexes]
        self.assertIn(['email', 'is_active'], index_fields)
        self.assertIn(['date_joined'], index_fields)


class LoginFormTests(TestCase):
    """Test LoginForm optimizations."""

    def test_login_form_excludes_is_active(self):
        """Verify that is_active is not in the form fields."""
        form = LoginForm()
        self.assertNotIn('is_active', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('password', form.fields)


class SignupFormTests(TestCase):
    """Test SignupForm improvements."""

    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        }

    def test_signup_form_valid(self):
        """Test that valid signup form saves correctly."""
        form = SignupForm(data=self.user_data)
        self.assertTrue(form.is_valid())

    def test_signup_form_password_mismatch(self):
        """Test that password mismatch is caught."""
        data = self.user_data.copy()
        data['confirm_password'] = 'DifferentPassword123!'
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

    def test_signup_form_duplicate_email(self):
        """Test that duplicate email is caught."""
        User.objects.create_user(email='test@example.com', password='password123')
        form = SignupForm(data=self.user_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class LoginViewTests(TestCase):
    """Test login view optimizations."""

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('authentication:login')
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_login_view_get(self):
        """Test that GET request returns form."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_login_view_post_valid_credentials(self):
        """Test login with valid credentials."""
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        # Should redirect to homepage or 2FA setup
        self.assertEqual(response.status_code, 302)

    def test_login_view_post_invalid_credentials(self):
        """Test login with invalid credentials."""
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_login_view_missing_fields(self):
        """Test login with missing fields."""
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 200)


class SignupViewTests(TestCase):
    """Test signup view."""

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('authentication:signup')

    def test_signup_view_get(self):
        """Test that GET request returns form."""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_signup_view_post_valid(self):
        """Test signup with valid data."""
        response = self.client.post(self.signup_url, {
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())
