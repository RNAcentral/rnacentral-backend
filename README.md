# rnacentral-backend

## Installation

1. Clone Git repository and access the directory:
  ```
  git clone --recursive https://github.com/RNAcentral/rnacentral-backend.git
  cd rnacentral-backend
  ```

2. Using the `.env-example` file as a template, create the `.env` file and change the variables as desired.

3. Create and activate a Virtual Environment
  ```
  python -m venv env
  source env/bin/activate
  ```

4. Run the app using:
  ```
  cd backend
  uvicorn main:app --reload
  ```
