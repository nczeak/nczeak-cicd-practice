ARG APP_ENV=dev

# ---------------------
# Create build for file
# ---------------------
FROM mongo:4.4.6-bionic as build

# --- Install Python ---
RUN apt-get update \
    && apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev
RUN apt-get install -y sudo

# --- Install pymongo ---
RUN pip3 install pymongo

RUN apt-get install -y parallel

# ----------------------
# Create dev environment
# ----------------------
FROM build as install-dev

# -----------------------
# Create test environment
# -----------------------
FROM build AS install-test

# --- Install testing software ---
# install pytest
RUN pip3 install pytest
# install parallel for exiting Mongo after tests are complete
RUN apt-get install -y parallel

# --- Copy tests into working directory ---
COPY ./tests/test_create_mongo.py .
COPY ./tests/test_insert_mongo.py .

# -----------------------------
# Create production environment
# -----------------------------
FROM build AS install-prod

# ----------------------------
# Create specified environment
# ----------------------------
FROM install-${APP_ENV} as install

# -------------------
# Run dev environment
# -------------------
FROM install as run-dev

# --------------------
# Run test environment
# --------------------
FROM install as run-test

# --- Define the username and passwork as environment variables ---
ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=password

# --- Run the tests in parallel to the server. End server when done. ---
COPY ./wait-for-it.sh .
RUN chmod +x ./wait-for-it.sh
RUN parallel -j2 --halt now,success=1 ::: 'sudo ./wait-for-it.sh "localhost:27017" -- pytest ./test_create_mongo.py && pytest ./test_insert_mongo.py' '/bin/sh ./docker-entrypoint.sh'

# --------------------
# Run test environment
# --------------------
FROM install as run-prod

# -------------------------
# Run specified environment
# -------------------------
FROM run-${APP_ENV} as run