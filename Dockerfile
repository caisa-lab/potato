FROM python:3.11-slim-bookworm

WORKDIR /app

COPY ./potato /app/potato
COPY ./requirements.txt /app/requirements.txt
COPY ./task /app/task


RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 8080

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]