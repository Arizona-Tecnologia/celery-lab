# celery-lab

A simple project for testing Celery task rejections. It was originally created
to help reproduce a [possible bug in
Celery](https://github.com/celery/celery/issues/2944).

## Set up

Start/run RabbitMQ on a docker container.

```
$ docker pull rabbitmq:3-management
$ docker run -v /etc/localtime:/etc/localtime:ro -p 5672:5672 -p 15672:15672 \
-d --hostname rabbitlab --name rabbit-lab rabbitmq:3-management
```
To access RabbitMQ web interface: http://localhost:15672/

Start/run Celery Flower on a docker container.

```
$ docker pull rabbitmq:3-management
$ docker run -p 5555:5555 -d --name flower-lab --link rabbit-lab:rabbit \
-e CELERY_BROKER_URL=amqp://guest:guest@rabbit:5672// \
iserko/docker-celery-flower --broker_api=http://guest:guest@rabbit:15672/api/
```

To access Celery Flower web interface: http://localhost:5555/
Create the dead letter exchange and dead letter queue.

```
$ ./config-queues.sh
```

Create and activate the virtual environment.

```
$ virtualenv-3.4 venv
$ source venv/bin/activate
```

Install the dependencies.

```
$ pip install -r requirements.txt
```

Startup a Celery worker.

```
$ celery -A lab worker -l info
```

Invoke the Celery worker using a client.

```
$ python divzero.py
```

Monitor the results on Celery Flower.

With Celery 3.1.16, the `Reject`
exception causes the message to be rejected (and routed to
`queue-DeadLetter`) and the task state to be set to `FAILURE`.

With Celery 3.1.19 (the latest version as of December 1st, 2015), the `Reject`
exception causes the message to be rejected (and routed to
`queue-DeadLetter`) but the task state is kept the same, ie. `STARTED`.
