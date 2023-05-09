#!/usr/bin/env bash

docker build -t nokal/wp4-platform-plc-mock:$(poetry version -s) . 
