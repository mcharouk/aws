FROM python:3.13-slim
WORKDIR /myDir
COPY . /myDir
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]