# Python & Django Interview Assignment

# Installation instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/MinatoNami/django-assignment.git
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

### Tasks attempted:

1. Installed PostgreSQL17 locally (using HomeBrew on MacOS)
2. Connected to local database and tested connection.
3. Created table for storing X-Y coordinates that consists of 2 columns (X and Y). Data format for both columns are DOUBLE PRECISION.
4. Performed insertion of dummy points into database.
5. Queried points from database
6. Deleted table
7. Setup Amazon RDS and configured database for public access (for ease of access, normal way is to connect via a VPC)
8. Created an Inbound rule on EC2 Secuirity Group for local access.
9. Tested connection and performed the tasks listed in Step 1-6

## Part 2

Django Project for this part is in the /DjangoPoints folder

### Tasks attempted:

1. Setup Django project
2. Connect Django to PostgreSQL from Part 1
3. Setup a static site to add/delete points, and retrieve points to be plotted on ChartJS for visualizations.
4. Added feature to support CSV upload of X,Y points (part 3), to aid me in visualizing the data.

## Part 3

File used for finding outliers is outlier.py.
For finding outliers, there are many methods to define what is an "outlier". Typically, you need to define some threshold or value to define an outlier. For this task, I am tasked to detect outliers from a curve. This can be done by fitting the data on a Polynomial Regression curve (might need to experiement with the number of degrees), as well as using the RANSAC from Sklearn's library. For the Polynomial Regression, I have defined an outlier as a value that is more than 2 STD away from the plotted curve.

### Tasks attempted:

1. Create functions for both Polynomial Regression and RANSAC.
2. Enabled CSV upload for ease of use
3. Plotted subplots of both methods to show outliers and the curve
