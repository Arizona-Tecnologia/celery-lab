#! /bin/bash

RABBIT_HOST=localhost
RABBIT_PORT=15672

if [ ! -f rabbitmqadmin ]
then
  wget http://$RABBIT_HOST:$RABBIT_PORT/cli/rabbitmqadmin
fi

if [ ! -x rabbitmqadmin ]
then
  chmod +x rabbitmqadmin
fi

DEADLETTER_EXCHANGE=exchange-DeadLetter
DEADLETTER_QUEUE=queue-DeadLetter

./rabbitmqadmin --host=$RABBIT_HOST --port=$RABBIT_PORT --vhost=/ declare exchange name=$DEADLETTER_EXCHANGE type=fanout durable=true
./rabbitmqadmin --host=$RABBIT_HOST --port=$RABBIT_PORT --vhost=/ declare queue name=$DEADLETTER_QUEUE durable=true
./rabbitmqadmin --host=$RABBIT_HOST --port=$RABBIT_PORT --vhost=/ declare binding source=$DEADLETTER_EXCHANGE destination_type=queue destination=$DEADLETTER_QUEUE
