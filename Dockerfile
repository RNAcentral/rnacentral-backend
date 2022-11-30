# create image to export requirements
FROM python:3.10-slim AS poetry

# build dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
        gcc \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN python -m pip install --no-cache-dir --upgrade poetry==1.2.1

# copy dependencies
COPY poetry.lock pyproject.toml ./

# create a requirements file
RUN poetry export -f requirements.txt --without-hashes -o /tmp/requirements.txt


# create rnacentral image
FROM python:3.10-slim as rnacentral

ENV \
    # python
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # RNAcentral
    RNACENTRAL_HOME="/srv/rnacentral/rnacentral-backend"

# create folder and set work directory
RUN mkdir -p $RNACENTRAL_HOME
WORKDIR $RNACENTRAL_HOME

# install requirements
COPY --from=poetry /tmp/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# copy project
COPY . .

EXPOSE 8001
