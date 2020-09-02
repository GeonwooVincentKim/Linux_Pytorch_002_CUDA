# Executes from 'Adminstrator'
from Adminstrator/pytorch

run mkdir /FlaskAPI
workdir /FlaskAPI

copy requirements.txt /FlaskAPI
run pip install --no-cache-dir -r requirements.txt

copy app /FlaskAPI/app

copy taco_burrito.prm /FlaskAPI
copy wsgi.py /FlaskAPI

env PRM_FILE /FlaskAPI/taco_burrito.prm

cmd gunicorn --access-logfile - \
             -b 0.0.0.0:8000 -w 4 \
             --preload wsgi:app
