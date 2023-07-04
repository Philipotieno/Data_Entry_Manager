[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Philipotieno/Data_Entry_Manager/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Philipotieno/Data_Entry_Manager/tree/main) [![codecov](https://codecov.io/gh/Philipotieno/Data_Entry_Manager/branch/main/graph/badge.svg?token=2NRXWZLTZ2)](https://codecov.io/gh/Philipotieno/Data_Entry_Manager)


# Data Entry Manager

## [Database Design](https://github.com/Philipotieno/Data_Entry_Manager/blob/main/DataBaseDesign.md)


### How set up and run the aplication

To start and run the local development server,

1. Clone this repo:
    ```
    $ git clone https://github.com/Philipotieno/Data_Entry_Manager.git
    ```

2. Initialize and activate a virtualenv:
    ```
    $ python3 -m venv venv
    ```

    ```
    $ source venv/bin/activate
    ```
3. Install the dependencies:
    ```
    $ pip install -r requirements.txt
    ```

4. Migrate:
    ```
    $ ./manage.py migrate
    ```

5. Run the development server:
    ```
    $ ./manage.py runserver 8000
    ```

6. Read the docs:
        Navigate to page 
            `http://localhost:8000/redoc`

7. Test api using swagger:
        Navigate to page
            `http://localhost:8000/swagger`


8. Running tests:
    ```
    $ pytest
    ```

![Tests](https://github.com/Philipotieno/Data_Entry_Manager/blob/main/tests.png)