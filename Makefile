dependences:
	echo "Makefile microservicio\n"
	echo "language: python version 3.6.6"
	echo "install dependences"
	pip3 install -r requirements.txt

services:
	echo "service postgresql"
	postgresql

script: 
	echo "run tests"
	cd ./test && pytest -v test.py 


ini_ap:
	echo "ini app"
	cd ./src/ && sudo  gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:80
	

stop_app:
	echo "stop app"
	sudo pkill -f gunicorn