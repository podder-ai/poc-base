#!/usr/bin/env bash

autopep8 --in-place --recursive --aggressive .
yapf --in-place --recursive .
autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive .
isort --recursive .
flake8 --ignore=E501,F811 .