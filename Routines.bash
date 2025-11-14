#!/usr/bin/env bash
set -e -x

PYTEST_FLAGS="-o log_cli=true -o log_cli_level=INFO"

case $1 in
  deps_devel)
    pushd JerProOdooLogParser/
    python3 -m pip install --upgrade -r requirements.txt
    popd
    ;;
  
  install_program)
    pushd JerProOdooLogParser/
    pip install -e .
    popd
    ;;
  
  test_unit)
    pushd JerProOdooLogParser/
    pytest $PYTEST_FLAGS
    popd
    ;;
  
  reinvent_wheel)
    python3 -m pip install --upgrade build
    pushd JerProOdooLogParser/
    python3 -m build
    popd
    ;;
  publish_wheel)
    python3 -m pip install --upgrade twine
    pushd JerProOdooLogParser/
    python3 -m twine upload --repository pypi dist/*
    popd
    ;;
    
  *)
    echo "Unknown routine name: $1"
    exit -1
    ;;
esac
