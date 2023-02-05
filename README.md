# Cocoon Creation
## Description
Cocoon Creation backend created with django and mysql

* Clone this project
    ```bash
    git clone https://github.com/solomond6/cocooncreation.git
    ```

* Install Mysql database

* Clone this project
    ```bash
    git clone git@github.com:MooveAfrica/moove-unified-api.git
    ```
* Enter project root directory
    ```bash
    cd Cocooncreation
    ```
* Install packages
    ```bash
    pip install -r requirements.txt
    ```
* In the cocooncreation folder, open `settings/development` change the mysql connection details to your local mysql connection details
    ```

* Migrate tables to postgres database
    ```bash
    python manage.py migrate
    ```

* Start the application
    ```bash
    python manage.py runserver
    ```

* Admin Login
    ```bash
    Username: admin@example.com
    Password: 1234567890
    ```

* Api Routes
    ```bash
    /api/categories
    /api/authors
    /api/articles
    ```