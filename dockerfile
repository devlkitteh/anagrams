FROM python:latest

WORKDIR /user/py_program
COPY interview.py .

CMD ["python", "./interview.py"]
