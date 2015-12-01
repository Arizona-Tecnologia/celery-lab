# -*- coding: utf-8 -*-

from celery.exceptions import Reject
from celery.utils.log import get_task_logger
from .celery import app

logging = get_task_logger(__name__)

@app.task(bind=True, max_retries=0)
def invert(*args, **kwargs):
    try:
        x = float(kwargs['x'])
        logging.info("x=%f", x)
        result = 1.0 / float(x)
        logging.info("Result=%f", result)
    except Exception as e:
        raise Reject(e) from e
