#!/bin/bash

if [[ "_${KRAFTI_VERSION}" = "_" ]]; then
    echo "Need to set version with export KRAFTI_VERSION"
    exit 1
fi

echo "Building Version ${KRAFTI_VERSION}"

docker build -t fthievent/krafti:"${KRAFTI_VERSION}" .

echo "Tagging ${KRAFTI_VERSION} to latest"
docker tag fthievent/krafti:"${KRAFTI_VERSION}" fthievent/krafti:latest

echo "pushing ${KRAFTI_VERSION}"
docker push fthievent/krafti:"${KRAFTI_VERSION}"

echo "pushing latest"
docker push fthievent/krafti:latest

unset KRAFTI_VERSION
echo "done"