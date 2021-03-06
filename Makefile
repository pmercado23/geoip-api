# Geoip-api Makefile
# Maintained by: Peter

CURDIR = $(realpath $(dir $(firstword $(MAKEFILE_LIST))))

# Rules
all:: install

create_env:
	cd ${CURDIR}
	virtualenv -p python3.6 env

install_requirements:
	(. ${CURDIR}/env/bin/activate && pip3 install -r requirements.txt)

devinstall:	create_env install_requirements

install:	create_env
	(. ${CURDIR}/env/bin/activate && python3.6 setup.py install)

clean:
	rm -rf ${CURDIR}/build ${CURDIR}/dist ${CURDIR}/*.egg-info

cleanall:	clean
	# Nuke the env
	rm -rf ${CURDIR}/env

deploy_gcp: build_kube_docker delpoy_kube_deployment delpoy_kube_service delpoy_kube_cron

docker_run: build run_docker

local_run: update_db_local run_server_local

build:
	docker build -t tpgkiwi/starry:1.0.0 .
	docker push tpgkiwi/starry:1.0.0

run_docker:
	docker run -it -p 8000:8000 tpgkiwi/starry:1.0.0

run_server_local:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py runserver

update_db_local:
	${CURDIR}/env/bin/python3 ${CURDIR}/setup_db.py

migrations_local:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py makemigrations

migrate_local:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py migrate

showmigrations_local:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py showmigrations

shell_local:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py shell

test:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py test


build_kube_docker:
	docker build -t gcr.io/test-project-245416/geoip-app .
	docker push gcr.io/test-project-245416/geoip-app

delpoy_kube_service:
	kubectl create -f deploy/service-def.yaml

delpoy_kube_deployment:
	kubectl create -f deploy/deployment-def.yaml

delpoy_kube_cron:
	kubectl create -f deploy/cron-job-def.yaml