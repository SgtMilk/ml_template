# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

# RUN COMMANDS

train:
	python3 train.py

test:
	python3 train.py


# ENVIRONMENT SETUP COMMANDS

setup:
	pip3 install -r requirements.txt

docker-setup:
	pip3 install -r ./.docker/requirements.txt

fetch-data:
	python3 setup.py

# Requires pip-tools
generate-reqs:
	pip-compile requirements.in
	pip-compile ./.docker/requirements.in
