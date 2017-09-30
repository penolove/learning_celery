learning celery

all the commands were execute in this folder, besides setting user and password

# install celery
```
pip install celery
```

# install RabbitMQ
```
sudo apt-get install rabbitmq-server
```

here are some setting for rabbitmq-server
### ref:https://tests4geeks.com/python-celery-rabbitmq-tutorial/
```
# add user 'jimmy' with password 'jimmy123'
$ rabbitmqctl add_user jimmy jimmy123
# add virtual host 'jimmy_vhost'
$ rabbitmqctl add_vhost jimmy_vhost
# add user tag 'jimmy_tag' for user 'jimmy'
$ rabbitmqctl set_user_tags jimmy jimmy_tag
# set permission for user 'jimmy' on virtual host 'jimmy_vhost'
$ rabbitmqctl set_permissions -p jimmy_vhost jimmy ".*" ".*" ".*"

```

# install monitor UI flower
```
pip install flower
celery -A test_celery flower
```

# learning_celery
