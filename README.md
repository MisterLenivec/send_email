# Send_email

### Sending Asynchronous Email Messages
### Practice Celery + Django3 and Redis in Docker


#### Run redis on docker:
```
docker run -d -p 6379:6379 redis
```

#### Run django server:
```
python manage.py runserver
```

#### Run the Celery worker server:
```
celery -A send_email worker -l info
```

#### Run the periodic task scheduler:
```
celery -A send_email beat -l info
```
