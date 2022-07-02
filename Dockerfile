ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Setup working dorectory
WORKDIR /app

# We are copying this before everything else because it's faster
COPY ./.docker/requirements.txt /app/.docker/requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install -r /app/.docker/requirements.txt

# Copy the rest and install source data
COPY . .
RUN python3 setup.py

# Set environment variables

# Runtime operations (CMD)
