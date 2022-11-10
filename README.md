# rnacentral-backend

## Installation

1. Clone Git repository:

  ```
  git clone --recursive https://github.com/RNAcentral/rnacentral-backend.git
  ```

2. Run the app using [Docker](https://www.docker.com):

  ```
  docker-compose up --build
  ```

## Tests

To run all tests, use

  ```
  docker exec -it <container_id> python /backend/manage.py test sequence.tests
  ```
