ARG APP_ENV=dev

# ---------------------
# Create build for file
# ---------------------
FROM apache/airflow:2.1.0-python3.8 as build

# --- Install Python ---
RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev

# --- Install Python dependencies ---
RUN pip3 install -y apache-airflow

# ----------------------
# Create dev environment
# ----------------------
FROM build as install-dev

# -----------------------
# Create test environment
# -----------------------
FROM build AS install-test

# --- Install pytest ---
RUN pip3 install -y pytest

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

# --------------------
# Run test environment
# --------------------
FROM install as run-prod

# -------------------------
# Run specified environment
# -------------------------
FROM run-${APP_ENV} as run