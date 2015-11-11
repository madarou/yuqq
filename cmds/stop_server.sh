#!/bin/sh
source ./stop_uwsgi.sh uwsgi
sleep 3
source ./stop_nginx.sh
