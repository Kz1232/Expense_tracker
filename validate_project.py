#!/usr/bin/env python3
"""
Project Validation Script
Run this script to check the current state of the Expense Tracker project
and identify immediate issues that need attention.
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and return status"""
    if os.path.exists(filepath):
        return f"✅ {description}"
    else:
        return f"❌ {description} - FILE MISSING"

def check_file_empty(filepath, description):
    """Check if a file is empty (placeholder) and return status"""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read().strip()
            if not content or "# Create your" in content or content.count('\n') < 5:
                return f"🟡 {description} - PLACEHOLDER/EMPTY"
            else:
                return f"✅ {description} - HAS CONTENT"
    else:
        return f"❌ {description} - FILE MISSING"

def main():
    print("🔍 Expense Tracker Project Validation")
    print("=" * 50)
    
    # Project structure checks
    print("\n📁 PROJECT STRUCTURE:")
    print(check_file_exists("expense_tracker_project/manage.py", "Django manage.py"))
    print(check_file_exists("requirements.txt", "Requirements file"))
    print(check_file_exists("expense_tracker_project/expense_tracker_project/settings.py", "Django settings"))
    
    # Critical files that should have content
    print("\n📝 CORE APPLICATION FILES:")
    print(check_file_empty("expense_tracker_project/myapps/models.py", "Expense models"))
    print(check_file_empty("expense_tracker_project/myapps/views.py", "Expense views"))
    print(check_file_empty("expense_tracker_project/myapps/admin.py", "Admin registration"))
    print(check_file_exists("expense_tracker_project/myapps/forms.py", "Expense forms"))
    
    # Authentication files
    print("\n🔐 AUTHENTICATION FILES:")
    print(check_file_empty("expense_tracker_project/authentication/models.py", "User models"))
    print(check_file_empty("expense_tracker_project/authentication/views.py", "Auth views"))
    print(check_file_empty("expense_tracker_project/authentication/forms.py", "Auth forms"))
    
    # Test files
    print("\n🧪 TEST FILES:")
    print(check_file_empty("expense_tracker_project/authentication/tests.py", "Auth tests"))
    print(check_file_empty("expense_tracker_project/myapps/tests.py", "App tests"))
    
    # Static files and templates
    print("\n🎨 FRONTEND FILES:")
    print(check_file_exists("expense_tracker_project/myapps/templates/myapps/index.html", "Homepage template"))
    print(check_file_exists("expense_tracker_project/static", "Static files directory"))
    
    # Check for security issues
    print("\n🔒 SECURITY CHECKS:")
    settings_file = "expense_tracker_project/expense_tracker_project/settings.py"
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            content = f.read()
            if "django-insecure" in content:
                print("⚠️  Django secret key is insecure/hardcoded")
            if "EMAIL_HOST_PASSWORD" in content and "=" in content:
                print("⚠️  Email credentials are hardcoded in settings")
            if "DEBUG = True" in content:
                print("⚠️  Debug mode is enabled (OK for development)")
    
    # Database check
    print("\n🗄️  DATABASE:")
    db_file = "expense_tracker_project/db.sqlite3"
    if os.path.exists(db_file):
        size = os.path.getsize(db_file)
        print(f"✅ Database exists ({size} bytes)")
    else:
        print("❌ Database not found - run 'python manage.py migrate'")
    
    print("\n" + "=" * 50)
    print("📋 SUMMARY:")
    print("✅ = Working/Complete")
    print("🟡 = Needs implementation") 
    print("❌ = Missing/Broken")
    print("⚠️  = Security/Configuration issue")
    
    print(f"\n📄 See TODO.md, TECHNICAL_ISSUES.md, and PROJECT_STATUS.md for detailed task lists")

if __name__ == "__main__":
    main()