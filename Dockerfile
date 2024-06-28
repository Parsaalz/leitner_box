FROM python:3.9-slim
WORKDIR /app
RUN apt-get update -o Acquire::Retries=3 && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install -v --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=myproject.settings
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
