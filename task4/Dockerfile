FROM python:latest

WORKDIR /app
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install paho-mqtt
COPY . ./
EXPOSE 1883
CMD [ "python3", "./public_from_file.py", "&", "python3", "./read_value_from_topic.py"]
