# Database Conventer with wxPython

A simple database conventer application with a graphical user interface (GUI) built using wxPython. The application connects to a MySQL database, retrieves table names, and displays them in a table/grid format. It allows users to select tables by checking a checkbox in the first column and saves the data of the selected tables in CSV format upon clicking the "Save" button.

## Requirements

- Python 3.9 or later
- wxPython 4.2.1a or later
- MySQL database

## Setup

1.  Install required Python packages:

    `$ pip install -r requirements.txt `

2.  Configure the database connection by editing the config.ini file:
    <?>

        [Database]

        host=localhost
        user=username
        password=user_password
        database=database_name

3.  Run the application:

    `$ python main.py `

## Usage

1. Launch the application.
2. Select the desired tables by checking the checkboxes in the first column.
3. Click the "Save" button to export the data of the selected tables in CSV format.

## Notes

- The application uses wxPython for the graphical user interface and MySQL Connector/Python for database connectivity.

- The first column displays checkboxes for table selection, and the second column shows the table names.

- CSV files are saved in the working directory, with each table's data saved in a separate file named after the table.

## Image

![img](https://github.com/Csikito/database_converter_csv/assets/84712542/fd5b3cfc-a021-4665-b7f2-f3ea41d25ad0)
