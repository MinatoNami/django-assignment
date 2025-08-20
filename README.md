# Python & Django Interview Assignment

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd django-assignment
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   cd DjangoPoints
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

# Environment variables

Clone env.examples and rename it to your respective environments (.local, .prod, etc)

# Coding Challenges

Postgresql 17 will be used for both local and RDS deployments.

## Part 1

File used for Python interaction with Postgresql is postgresql_interact.py.

## Part 2

Django Project for this part is in the /DjangoPoints folder

## Part 3

File used for finding outliers is outlier.py
