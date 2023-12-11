from configparser import ConfigParser

def load_database_config():

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