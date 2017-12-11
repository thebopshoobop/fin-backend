FROM python:3.6

# create working directory
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/py

# install virtualenv globally
RUN pip install virtualenv

# create app user
RUN groupadd -r -g 2000 app
RUN useradd -r -u 2000 -g 2000 -s /usr/bin/nologin app
RUN chown -R 2000:2000 /usr/src
USER app

# switch to working directory
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN virtualenv /usr/src/py
RUN /usr/src/py/bin/pip install --no-cache-dir -r requirements.txt

# add app
ADD . /usr/src/app

# run server
CMD /usr/src/py/bin/python manage.py run -h 0.0.0.0
