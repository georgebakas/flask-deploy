FROM python:3.7.2

RUN pip install pipenv

# Add an application folder to the container
ADD . /flask-deploy

WORKDIR /flask-deploy

# Install all dependencies using Pipenv
#RUN pipenv install --system --skip-lock

RUN pip install flask flask-restful flask-sqlalchemy flask-migrate celery gunicorn[gevent]
#RUN pip install gunicorn[gevent]
# Expose TCP port 5000 to the host
EXPOSE 5000

# Set the container’s default startup command to a Gunicorn call
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app \
    --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info