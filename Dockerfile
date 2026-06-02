FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
EXPOSE 8501

CMD ["streamlit", "run", "app/dashboard.py", "--server.address=0.0.0.0"]
