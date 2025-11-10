#!/bin/bash

# Serve Jekyll site with Podman
# Usage: ./serve.sh

podman run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  --publish 4000:4000 \
  --publish 35729:35729 \
  -it \
  docker.io/jekyll/jekyll:4 \
  jekyll serve --watch --force_polling --livereload
