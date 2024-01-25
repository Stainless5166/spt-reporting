# Dockerfile
FROM python:3.11
LABEL authors="williamh"
LABEL version="alpha"
LABEL description="Docker image for building the SPT-Reporting AppImage"


# Set work directory in the container
WORKDIR /app

# Install appimage-builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    python3-pip python3-setuptools patchelf desktop-file-utils  \
    libgdk-pixbuf2.0-dev fakeroot strace python3-click python3-tabulate  \
    python3-pip python3-packaging python3-jinja2 python3-pyparsing  \
    python3-toml python3-click python3-coloredlogs python3-pyelftools  \
    elfutils wget squashfs-tools python3-pytest python3-pytest-cov

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application files and the AppImageBuilder.yml into the container
COPY . .

# Run all tests
RUN python -m unittest discover -s tests

# Make AppImage
RUN appimage-builder

# Copy the AppImage to the host
RUN cp SPT-Reporting*.AppImage /app/SPT-Reporting.AppImage

# Run Tests
# include any steps needed to test your application