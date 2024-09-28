#!/bin/bash

kill -9 $(ps -ef | grep 'someip_app/services' | grep -v grep | awk '{print $2}')


