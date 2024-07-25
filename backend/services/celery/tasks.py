from celery import Celery

celery = Celery('varif', broker='redis://localhost:15672')


@celery.task
def send_veryf_account():
    return 'Hello World!'