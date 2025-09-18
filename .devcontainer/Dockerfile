# Use Ubuntu 22.04 as base
FROM ubuntu:22.04

# Install dependencies
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

# Prepare MariaDB socket
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Create workspace and fix permissions
RUN mkdir -p /workspace && chown -R vscode:vscode /workspace

# Set working directory
WORKDIR /workspace

# Copy scripts and requirements from repo root
COPY create_db.py /workspace/create_db.py
COPY run_live_debug.py /workspace/run_live_debug.py
COPY requirements.txt /workspace/requirements.txt

# Install Python dependencies including watchdog and debugpy
RUN pip3 install -r requirements.txt debugpy watchdog

# Switch to vscode user
USER vscode
