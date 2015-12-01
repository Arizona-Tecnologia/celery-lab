# -*- coding: utf-8 -*-

from kombu import Exchange, Queue
from celery import Celery

# Broker AMQP
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

app = Celery('lab', broker=BROKER_URL)

app.conf.update(
    CELERY_IMPORTS = ('lab.tasks'),
    # CELERY_RESULT_BACKEND = 'rpc',
    # CELERY_RESULT_SERIALIZER = 'json',

    CELERY_QUEUES = (
        Queue('queue-Lab',
            exchange = Exchange('exchange-Lab', type='direct'),
            routing_key = 'key-Lab',
            queue_arguments = {'x-dead-letter-exchange':'exchange-DeadLetter'}
        ),
    ),

    CELERY_ROUTES = {
        'lab.tasks.invert': {
            'exchange': 'exchange-Lab',
            'routing_key': 'key-Lab'
        },
    },

    # APP Configuration
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_TIMEZONE = 'America/Sao_Paulo',
    CELERY_ENABLE_UTC = True,
    CELERY_DISABLE_RATE_LIMITS = True,
    CELERY_ACKS_LATE = True,
    CELERYD_PREFETCH_MULTIPLIER = 1,
    CELERY_IGNORE_RESULT = True,
    CELERYD_CONCURRENCY = 1,
    CELERY_ACCEPT_CONTENT = ['json']
)

#celery -A lab worker -l info
