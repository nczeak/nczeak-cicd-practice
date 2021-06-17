ARG APP_ENV=dev

# ---------------------
# Create build for file
# ---------------------
FROM mongo:4.4.6-bionic as build

# --- Install Python ---
RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev

# --- Install pymongo ---
RUN pip3 install pymongo

# ----------------------
# Create dev environment
# ----------------------
FROM build as install-dev

# -----------------------
# Create test environment
# -----------------------
FROM build AS install-test

# --- Install pytest ---
RUN pip3 install pytest

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

ENV MONGO_INITDB_ROOT_USERNAME=mongoadmin
ENV MONGO_INITDB_ROOT_PASSWORD=password

# --------------------
# Run test environment
# --------------------
FROM install as run-prod

# -------------------------
# Run specified environment
# -------------------------
FROM run-${APP_ENV} as run