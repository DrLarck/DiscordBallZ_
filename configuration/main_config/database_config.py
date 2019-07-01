'''
Manages the variables needed to create the connection to the database.

Last update: 30/06/19
'''

# Dependancies

import os

# Authentification

DB_USER = os.environ['DBZ_DB_USER']  # The username needed to connect to the database
DB_HOST = os.environ['DBZ_DB_HOST']  # The adress of the host
DB_PASSWORD = os.environ['DBZ_DB_PASSWORD']  # The password of the database
DB_NAME =  'dev_dbz3' #os.environ['DBZ_DB_NAME']  # The name of the database
DB_PORT = '5432'  # By default, the PostgreSQL's port is the 5432