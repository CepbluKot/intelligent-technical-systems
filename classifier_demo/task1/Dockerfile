FROM pypy:latest

WORKDIR /app
RUN /opt/pypy/bin/pypy -m pip install --upgrade pip
COPY . ./
CMD [ "pypy3", "./main.py"]