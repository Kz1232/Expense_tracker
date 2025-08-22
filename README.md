# Expense Tracker

A Django-based personal expense tracking application with user authentication and two-factor authentication support.

## 🚧 Development Status

**Current State:** Early Development - Authentication system complete, core expense tracking features in development.

For detailed information about the project status and remaining tasks, see:
- 📋 [**TODO.md**](TODO.md) - Complete list of features to implement
- 🔧 [**TECHNICAL_ISSUES.md**](TECHNICAL_ISSUES.md) - Code-level tasks and technical debt
- 📊 [**PROJECT_STATUS.md**](PROJECT_STATUS.md) - Current progress overview

## Quick Setup

To use this app simply follow the below steps:

1. Clone the repo or download in zip file 

2. Create a python environment inside the downloaded or cloned directory:
```bash
python -m venv env
```

3. Activate the virtual environment:
```bash
# Windows
env\Scripts\activate

# macOS/Linux
source env/bin/activate
```

4. Install the requirements.txt using following command:
```bash
pip install -r requirements.txt
```

5. Migrate the required tables using given commands:
```bash
cd expense_tracker_project
python manage.py migrate
```

6. Run the site:
```bash
python manage.py runserver
```

## Current Features ✅

- ✅ User registration and authentication with email
- ✅ Password reset via email
- ✅ Two-factor authentication (2FA) support
- ✅ Basic user dashboard
- ✅ Secure session management

## Planned Features 🚧

- 🔄 Core expense tracking (amount, date, description, category)
- 🔄 Expense categories and management
- 🔄 Monthly/yearly expense reports
- 🔄 Budget tracking and alerts
- 🔄 Data import/export functionality
- 🔄 Responsive web interface
- 🔄 Search and filtering capabilities

## Contributing

This project is under active development. Check the [TODO.md](TODO.md) file for tasks that need to be completed. Good first issues include:

1. Creating the core Expense model
2. Adding CSS styling to templates  
3. Writing unit tests for authentication
4. Creating basic expense management views

## Security Note

⚠️ **Important:** This application is in development and contains hardcoded secrets in `settings.py`. Do not deploy to production without proper configuration of environment variables and security settings.
