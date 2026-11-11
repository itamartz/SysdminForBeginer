FROM python:3.12-slim
WORKDIR /app
COPY app/requirements.txt app/
RUN pip install --no-cache-dir -r app/requirements.txt
COPY app app
COPY curriculum curriculum
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "2", "--timeout", "300", "--chdir", "app", "app:app"]
