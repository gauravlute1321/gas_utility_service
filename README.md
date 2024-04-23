
# Gas Utility Service Django Application

This Django application provides consumer services for gas utilities, allowing customers to submit service requests online, track the status of their requests, and view their account information. It also includes tools for customer support representatives to manage requests and provide support to customers.

## Features

- Service requests: Customers can submit service requests online, selecting the type of service request, providing details, and attaching files.
- Request tracking: Customers can track the status of their service requests, including submission and resolution dates.
- Account information: Customers can view their account information.
- Management tools: Customer support representatives have tools to manage service requests and provide support.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gas_utility_service.git
   cd gas_utility_service

2. Install dependencies:
--------bash-------------
pip install -r requirements.txt

3. Apply database migrations:
-------bash----------
python manage.py makemigrations
python manage.py migrate

4.Create a superuser (for accessing the admin panel):
--------bash--------------
python manage.py createsuperuser

5.Run the development server:
--------bash-------------
python manage.py runserver

6.Access the application in your web browser at http://127.0.0.1:8000/.


###Usage
Visit the admin panel at http://127.0.0.1:8000/admin/ to manage service requests and user accounts.
Customers can submit service requests at http://127.0.0.1:8000/submit-request/.
Customers can track their requests at http://127.0.0.1:8000/track-request/.
Customer support representatives can manage requests at http://127.0.0.1:8000/manage-requests/.
