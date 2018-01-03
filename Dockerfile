FROM python:3.6

# create working directory
RUN mkdir -p /usr/src/app

# create app user
RUN groupadd -r -g 2000 app && useradd -r -u 2000 -g 2000 -s /usr/bin/nologin app
RUN chown -R 2000:2000 /usr/src/app

# switch to working directory
WORKDIR /usr/src/app

# install requirements
ADD ./requirements.txt /usr/src/app/dev-requirements.txt
ADD ./dev-requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt -r dev-requirements.txt

# mount app source
ADD . /usr/src/app

# switch to app user
USER app

# run server
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
