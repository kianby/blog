site:
	./makesite.py

site_local:
	./makesite.py --params params-local.json

serve: site_local
	cd _site && python -m SimpleHTTPServer 2> /dev/null || python3 -m http.server

dock: site_local
	docker run --name bloglocal -p 80:80 -p 443:443 -v `pwd`/_site:/usr/share/nginx/html:ro -v `pwd`/nginx/nginx.conf:/etc/nginx/nginx.conf:ro -v `pwd`/nginx/dhparam.pem:/etc/nginx/dhparam.pem:ro -v `pwd`/ssl:/etc/nginx/ssl:ro nginx 

undock:
	docker stop bloglocal
	docker rm bloglocal

venv2:
	virtualenv ~/.venv/makesite
	echo . ~/.venv/makesite/bin/activate > venv
	. ./venv && pip install commonmark coverage

venv: FORCE
	python3 -m venv ~/.venv/makesite
	echo . ~/.venv/makesite/bin/activate > venv
	. ./venv && pip install commonmark coverage

test: FORCE
	. ./venv && python -m unittest -bv

coverage:
	. ./venv && coverage run --branch --source=. -m unittest discover -bv; :
	. ./venv && coverage report -m
	. ./venv && coverage html

clean:
	find . -name "__pycache__" -exec rm -r {} +
	find . -name "*.pyc" -exec rm {} +
	rm -rf .coverage htmlcov

FORCE:
