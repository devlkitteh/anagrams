FROM python:3.7-alpine

WORKDIR /user/py_program

COPY interview.py .
COPY dictionary.txt .

CMD ["python", "./interview.py"]
