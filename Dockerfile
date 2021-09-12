FROM python:3.6.7

WORKDIR usr/src/manual_launch
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
