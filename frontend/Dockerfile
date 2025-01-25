# syntax=docker/dockerfile:1

#############################
# 1) Base Image
#############################
FROM python:3.11-slim-bullseye AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # Other
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Prepend Poetry + venv to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


#############################
# 2) Builder Image
#    Installs Poetry
#############################
FROM python-base AS builder

# Install OS packages needed for building (curl for Poetry)
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy only Poetry files first to leverage caching
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

#############################
# 3) Development Stage
#    Installs only the "frontend" group (no dev)
#    You can still do hot-reload if you mount code
#############################
FROM builder AS development

# Install ONLY the 'frontend' group
RUN poetry install --only frontend

# Copy your actual frontend source code into /app
WORKDIR /app
COPY . /app

# Expose Streamlit’s default port
EXPOSE 8501

# This command starts Streamlit in dev-friendly mode (auto-reload)
CMD ["streamlit", "run", "frontend/main.py", "--server.address=0.0.0.0", "--server.port=8501"]


#############################
# 4) Production Stage
#    Installs only the "frontend" group
#    Leaves out dev dependencies
#############################
FROM builder AS production

# Again, install ONLY the 'frontend' group
RUN poetry install --only frontend

# Copy your actual frontend source code into /app
WORKDIR /app
COPY . /app

# Expose Streamlit’s default port
EXPOSE 8501

# Production entry command (essentially the same, but minimal deps)
CMD ["streamlit", "run", "frontend/main.py", "--server.address=0.0.0.0", "--server.port=8501"]
