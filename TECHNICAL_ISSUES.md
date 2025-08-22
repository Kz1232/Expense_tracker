# Technical Issues & Code Tasks

This document lists specific technical issues and code-level tasks that need immediate attention.

## 🚨 Critical Issues

### Security Concerns
- [ ] **Remove hardcoded email credentials from settings.py**
  - Current: Email credentials are exposed in `settings.py`
  - Solution: Move to environment variables or secure configuration
  - File: `expense_tracker_project/expense_tracker_project/settings.py` lines 145-146

- [ ] **Secret Key Security**
  - Current: Django secret key is hardcoded and marked as insecure
  - Solution: Generate new secret key and move to environment variables
  - File: `expense_tracker_project/expense_tracker_project/settings.py` line 23

### Database Issues
- [ ] **Empty Models Files**
  - Current: `myapps/models.py` is completely empty
  - Impact: No core expense tracking functionality
  - Action: Implement Expense, Category, Budget models

- [ ] **Missing Admin Registration**
  - Current: `myapps/admin.py` has no model registrations
  - Impact: No admin interface for expense management
  - Action: Register models in admin interface

### Code Quality Issues
- [ ] **Empty Test Files**
  - Files: `authentication/tests.py`, `myapps/tests.py`
  - Issue: No test coverage for any functionality
  - Risk: No validation of code functionality

- [ ] **Incomplete URL Configuration**
  - Current: Only basic homepage URL in myapps
  - Missing: All expense-related URLs and views

## 🔧 Immediate Code Tasks

### Models Layer
- [ ] **Create Expense Model in `myapps/models.py`**
  ```python
  # Suggested implementation
  class Expense(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      amount = models.DecimalField(max_digits=10, decimal_places=2)
      description = models.TextField()
      date = models.DateField()
      category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- [ ] **Create Category Model in `myapps/models.py`**
  ```python
  # Suggested implementation  
  class Category(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField(blank=True)
      color = models.CharField(max_length=7, default='#000000')  # Hex color
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
  ```

### Views Layer
- [ ] **Enhance `myapps/views.py`**
  - Current: Only basic homepage view
  - Needed: CRUD views for expenses and categories
  - Add proper error handling and user authentication checks

### Templates Layer  
- [ ] **Improve `myapps/templates/myapps/index.html`**
  - Current: Very basic HTML with minimal functionality
  - Needed: Professional dashboard layout
  - Add: Quick expense entry, recent transactions, spending summary

### Forms Layer
- [ ] **Create `myapps/forms.py`**
  - Missing: File doesn't exist
  - Needed: ExpenseForm, CategoryForm for data entry
  - Add: Proper validation and user experience

### URL Configuration
- [ ] **Expand `myapps/urls.py`**
  - Current: Only homepage URL pattern
  - Needed: Complete URL structure for expense management

## 🔍 Code Review Findings

### Authentication App Issues
- [ ] **LoginForm field inclusion**
  - File: `authentication/forms.py` line 11
  - Issue: `is_active` field included in form (should not be user-editable)
  - Fix: Remove `is_active` from fields list

- [ ] **Missing Form Validation**
  - Multiple forms lack comprehensive validation
  - Add client-side and server-side validation

### Static Files Configuration
- [ ] **Missing Static Files Setup**
  - No static files directory structure
  - No CSS, JavaScript, or image assets
  - Need to configure `STATIC_ROOT` and `STATICFILES_DIRS`

### Template Issues
- [ ] **No Base Template**
  - Templates lack consistent layout
  - No shared CSS/JavaScript includes
  - Create `base.html` template

- [ ] **Hard-coded URLs**
  - Templates use hard-coded URL patterns
  - Should use Django URL naming with `{% url %}` tags

## 🧪 Testing Tasks

### Unit Tests Needed
- [ ] **Model Tests**
  ```python
  # Example test structure needed
  class ExpenseModelTest(TestCase):
      def test_expense_creation(self):
          # Test expense model creation and validation
      
      def test_expense_str_method(self):
          # Test string representation
  ```

- [ ] **View Tests**
  ```python
  # Example test structure needed  
  class ExpenseViewTest(TestCase):
      def test_expense_list_view(self):
          # Test expense listing functionality
      
      def test_expense_create_view(self):
          # Test expense creation
  ```

### Integration Tests Needed
- [ ] **User Workflow Tests**
  - Complete user registration and expense entry workflow
  - Authentication flow with two-factor authentication
  - Data persistence and retrieval tests

## 📱 Frontend Tasks

### UI/UX Improvements
- [ ] **Responsive Design**
  - Current templates not mobile-friendly
  - Add responsive CSS framework (Bootstrap/Tailwind)

- [ ] **Form Styling**
  - Forms lack proper styling and validation feedback
  - Add client-side validation and error messaging

- [ ] **Navigation Menu**
  - No navigation between different sections
  - Add consistent navigation across all pages

## 🔒 Security Tasks

### Input Validation
- [ ] **Form Security**
  - Ensure all forms have CSRF protection
  - Add input sanitization for user-generated content
  - Implement rate limiting for form submissions

### Permission Checks
- [ ] **View-level Permissions**
  - Ensure users can only access their own data
  - Add proper authorization checks in all views
  - Implement role-based access if needed

---

*Priority: Fix security issues first, then implement core models and views*
*Estimated Total Effort: 40-60 hours for basic functionality*