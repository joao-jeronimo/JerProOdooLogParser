#!/usr/bin/env bash
set -e -x

# Script parameters:
TORELEASE=$1

# Incrementing release on the pyproject.toml file:
pushd JerProOdooLogParser
sed -i -e "s/^version=.*$/version='$TORELEASE'/" pyproject.toml
popd

# Create the tag to trigger the new release:
git add .
git commit -m "New release v$TORELEASE"
git tag "v$TORELEASE"

# Push everything up:
git push
git push origin --tags
