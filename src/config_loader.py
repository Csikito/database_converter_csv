from configparser import ConfigParser


def load_database_config():
    """
    Load database connection configuration from the 'config.ini' file.

    Reads the 'config.ini' file using the ConfigParser module and extracts
    the database connection settings from the 'Database' section.

    Returns:
    dict: A dictionary containing the database connection settings with keys:
        - 'host': Hostname of the database server.
        - 'user': Database user.
        - 'password': Password for the database user.
        - 'database': Database name.

    Example:
        {'host': 'localhost', 'user': 'myuser', 'password': 'mypassword', 'database': 'mydatabase'}
    """

    # Read the configuration file
    config = ConfigParser()
    config.read('config/config.ini')

    # Database connection settings
    db_config = {
        'host': config.get('Database', 'host'),
        'user': config.get('Database', 'user'),
        'password': config.get('Database', 'password'),
        'database': config.get('Database', 'database'),
    }

    return db_config
