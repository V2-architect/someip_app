#!/bin/bash

sudo docker rm $(sudo docker ps --all | grep mn. | awk '{print $NF}')
