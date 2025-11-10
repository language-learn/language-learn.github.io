#!/bin/bash

# Serve Jekyll site with Podman
# Usage: ./serve.sh

echo "Setting up Jekyll environment..."

# Create cache directories if they don't exist
mkdir -p .jekyll-cache _site

# Fix permissions for all directories that Jekyll needs to read
chmod -R 755 . 2>/dev/null || true
chmod 777 .jekyll-cache _site 2>/dev/null || true

echo "Starting Jekyll server..."
echo "Site will be available at: http://localhost:4000"
echo "Press Ctrl+C to stop"
echo ""

podman run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  --publish 4000:4000 \
  -it \
  --security-opt label=disable \
  docker.io/jekyll/jekyll:latest \
  sh -c "cp Gemfile.local Gemfile && bundle install && jekyll serve --host 0.0.0.0 --watch --force_polling --config _config.yml,_config_local.yml"

# Reset permissions after
chmod 755 .jekyll-cache _site 2>/dev/null || true
