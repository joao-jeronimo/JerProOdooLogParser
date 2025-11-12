#!/usr/bin/env bash
set -e -x

PYTEST_FLAGS="-o log_cli=true -o log_cli_level=INFO"

case $1 in
  deps_devel)
    pushd JerProOdooLogParser/
    python3 -m pip install --upgrade -r requirements.txt
    python3 -m pip uninstall pytest-xdist pytest-parallel
    popd
    ;;
  
  test_unit)
    pushd JerProOdooLogParser/
    pytest $PYTEST_FLAGS
    popd
    ;;
  *)
    echo "Unknown routine name: $1"
    exit -1
    ;;
esac
