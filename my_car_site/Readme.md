# Generate a new django Secret Key if you get .env local file overwritten
# bellow commands work on a regular python console
# importing the function from utils
from django.core.management.utils import get_random_secret_key

# generating and printing the SECRET_KEY
print(get_random_secret_key())