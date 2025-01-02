FROM python:3.12-slim
WORKDIR /myDir
COPY . /myDir
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]