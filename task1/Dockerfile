FROM pypy:latest

WORKDIR /app
COPY requirements.txt requirements.txt
RUN /opt/pypy/bin/pypy -m pip install --upgrade pip
RUN pypy3 -m pip install -r requirements.txt
COPY . ./
CMD [ "pypy3", "./main.py"]