# Executes from 'Adminstrator'
from Adminstrator/pytorch

run mkdir /FlaskAPI
workdir /FlaskAPI

copy requirements.txt /FlaskAPI
run pip install --no-cache-dir -r requirements.txt

copy app /FlaskAPI/app

copy taco_burrito.prm /FlaskAPI
copy wsgi.py /FlaskAPI
