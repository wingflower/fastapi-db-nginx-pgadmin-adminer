FROM python:3.10-slim

WORKDIR /app/was

COPY ./requirements.txt /app/was/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /app/was/requirements.txt
 
#CMD ["python", "app/main.py"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
