from celery import Celery

app = Celery('test_celery',
             broker='amqp://jimmy:jimmy123@localhost/jimmy_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])

