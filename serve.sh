#!/bin/bash

# Serve Jekyll site with Podman
# Usage: ./serve.sh

# Create cache directories if they don't exist
mkdir -p .jekyll-cache _site

# Make them world-writable temporarily for the container
chmod 777 .jekyll-cache _site 2>/dev/null || true

podman run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  --publish 4000:4000 \
  -it \
  --security-opt label=disable \
  docker.io/jekyll/jekyll:latest \
  sh -c "jekyll serve --host 0.0.0.0 --watch --force_polling --config _config.yml,_config_local.yml"

# Reset permissions after
chmod 755 .jekyll-cache _site 2>/dev/null || true
