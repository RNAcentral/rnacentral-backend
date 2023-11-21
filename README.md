# rnacentral-backend

## Installation

1. Clone Git repository:

  ```
  git clone --recursive https://github.com/RNAcentral/rnacentral-backend.git
  ```

2. Using the local_settings_example.py file as a template, create the local_settings.py file
and change the variables as desired. You will need to set up another database, as the public database
uses a version of postgres that is no longer supported by newer versions of Django.

3. Run the app using [Docker](https://www.docker.com):

  ```
  docker-compose up --build
  ```

## Tests

To run all tests, use

  ```
  docker exec -it <container_id> python /backend/manage.py test sequence.tests
  ```

## Developer details

1. For QcStatusSerializer, using PrimaryKeyRelatedField instead of CharField avoids a 
new query to the database. Drf-spectacular will throw a [warning](https://stackoverflow.com/questions/63078096/django-rest-framework-why-does-primarykeyrelatedfield-document-as-a-string-in-t)
message though.