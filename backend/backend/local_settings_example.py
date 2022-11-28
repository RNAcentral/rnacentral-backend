SECRET_KEY = "your-secret-key"  # keep the secret key used in production secret!
DEBUG = True  # never deploy a site into production with DEBUG turned on
ALLOWED_HOSTS = ["*"]  # you might want to change this in production

# Change database if needed
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "db_name",
#         "USER": "user",
#         "PASSWORD": "password",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }
