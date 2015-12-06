#!/bin/sh
source ./stop_uwsgi.sh uwsgi
sleep 1
source ./stop_nginx.sh
