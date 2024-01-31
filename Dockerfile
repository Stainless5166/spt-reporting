# Dockerfile
FROM python:3.11.6
LABEL authors="williamh"
LABEL version="alpha"
LABEL description="Docker image for building the SPT-Reporting AppImage"

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    patchelf desktop-file-utils  \
    libgdk-pixbuf2.0-dev fakeroot strace wget squashfs-tools

# Set up the working directory in the container
WORKDIR /app

# Install pip, Poetry and appimage-builder
RUN pip install --upgrade pip
RUN pip install poetry appimage-builder

# Copy only requirements to cache them in docker layer
# The wildcards ensure both pyproject.toml and poetry.lock are copied
COPY pyproject.toml poetry.lock ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the rest of the code
COPY . .

# Make AppImage
RUN appimage-builder

# Copy the AppImage to the host
RUN cp SPT-Reporting*.AppImage /app/SPT-Reporting.AppImage

# Run the main file(script)
EXPOSE 8000
CMD python -m http.server 8000