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

run:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py runserver

update_db:
	${CURDIR}/env/bin/python3 ${CURDIR}/setup_db.py

migrations:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py makemigrations

migrate:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py migrate

showmigrations:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py showmigrations

shell:
	${CURDIR}/env/bin/python3 ${CURDIR}/manage.py shell


