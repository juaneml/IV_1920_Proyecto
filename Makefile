dependences:
	echo "Makefile microservicio\n"
	echo "language: python version 3.6.6"
	echo "install dependences"
	pip3 install -r requirements.txt
	pip3 install codecov
    	pip3 install pytest-cov
    	pip3 install python-coveralls
   	pip3 install coveralls

script: 
	echo "run tests"
	cd ./test && pytest -v test.py 
	coverage run test.py
  	coverage report -m
  	coverage xml

ini_ap:
	echo "ini app"
	cd ./src/ && sudo  gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:8000
	

stop_app:
	echo "stop app"
	sudo pkill -f gunicorn

logs_repo:
	echo "logs repo"
	git log	
