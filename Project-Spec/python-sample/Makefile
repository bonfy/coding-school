.PHONY: clean-pyc

AUTHOR := bonfy
PROJECT := project
DOCKER-CONTAINER := $(AUTHOR)-$(PROJECT)

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
run:
	docker run -v /data/docker/config/$(PROJECT):/config -v /data/docker/log:/log $(DOCKER-CONTAINER)
freeze:
	pipenv run pip3 freeze > req.txt
build:
	docker build -t $(DOCKER-CONTAINER) .
