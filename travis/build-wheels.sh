#!/bin/bash
set -e -x

cd /io

# Compile wheels
for PYBIN in /opt/python/cp3{6..8}*/bin; do
    "${PYBIN}/pip" install -r requirements/release.txt -r requirements/test.txt -r requirements/doc.txt -r requirements/default.txt
    "${PYBIN}/python" setup.py bdist_wheel
done

# Install packages and test
for PYBIN in /opt/python/cp3{6..8}*/bin; do
    "${PYBIN}/pip" install python-jgrapht --no-index -f /io/dist
    (cd /io; "${PYBIN}/pytest")
done
