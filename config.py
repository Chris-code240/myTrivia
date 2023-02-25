import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://eibfzduj:uKfVn4_KQslqeQL28_4iLKpDQebNWZ5f@mahmud.db.elephantsql.com/eibfzduj'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SESSION_COOKIE_DOMAIN = False