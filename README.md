<h1>Expense Tracker </h1>

To use this app simply follow the below steps :

1. Clone the repo or download in zip file 

2. create a python environment inside the downloaded or cloned directory:
```
py -m venv env
```

3. Install the requirements.txt using following command:
```
pip install -r requirements.txt
```

4. Configure environment variables:
```
cp expense_tracker_project/.env.example expense_tracker_project/.env
```
Edit the `.env` file with your actual SECRET_KEY and email credentials.

5. Migrate the required tables using given commands:
```
py manage.py migrate
```

6. Run the site:
```
py manage.py runserver
```

## Performance Improvements

This application has been optimized for better performance and security. See [PERFORMANCE_IMPROVEMENTS.md](PERFORMANCE_IMPROVEMENTS.md) for details on:
- Database indexing optimizations
- Form and view performance improvements
- Admin interface enhancements
- Security best practices with environment variables
