# RUN COMMANDS

train:
	python3 train.py

test:
	python3 train.py


# ENVIRONMENT SETUP COMMANDS

setup:
	pip3 install -r requirements.txt

# Requires pip-tools
generate_reqs:
	pip-compile requirements.in
	pip-compile ./.docker/requirements.in
