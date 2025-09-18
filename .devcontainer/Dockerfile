# Base image
FROM ubuntu:22.04

# Install MariaDB, Python3, pip, sudo
RUN apt-get update && apt-get install -y \
    mariadb-server \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user
RUN groupadd --gid 1000 vscode \
    && useradd -m -s /bin/bash --uid 1000 --gid 1000 vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# Setup MariaDB folder
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Set working directory
WORKDIR /workspace

# Copy devcontainer files
COPY .devcontainer/requirements.txt /workspace/requirements.txt
COPY .devcontainer/create_db.py /workspace/.devcontainer/create_db.py
COPY .devcontainer/run_live_debug.py /workspace/.devcontainer/run_live_debug.py

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set vscode user as default
USER vscode

# Command to start MariaDB and watch Python files
CMD sudo service mariadb start && python3 .devcontainer/run_live_debug.py
