FROM python:latest
COPY server.py /server.py
COPY server-default.py /server-default.py
ENTRYPOINT [ "python3","-u","server.py" ]
CMD [ "1","5", "sometext" ]