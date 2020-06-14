# Send_email

### Sending Asynchronous Email Messages
### Practice Celery + Flower +  Django3 and Redis on Docker


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

#### Run Flower:
```
flower -A send_email --port=5555
```

#### If you want the task to run at regular intervals
#### Run the periodic task scheduler:
```
celery -A send_email beat -l info
```

#### View Flower http://127.0.0.1:5555/
