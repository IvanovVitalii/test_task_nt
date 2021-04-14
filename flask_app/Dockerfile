FROM python:3.9.4
WORKDIR /usr/app
ADD . /usr/app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]