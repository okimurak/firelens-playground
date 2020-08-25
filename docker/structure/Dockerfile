FROM python:3.7-alpine
COPY requirements.txt /usr/src/myapp/
RUN pip3 install -r /usr/src/myapp/requirements.txt
COPY main.py /usr/src/myapp/
ENTRYPOINT [ "python", "/usr/src/myapp/main.py" ]