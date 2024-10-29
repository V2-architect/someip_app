#!/bin/bash

sudo docker stop $(sudo docker ps --all | grep mn. | awk '{print $NF}')
