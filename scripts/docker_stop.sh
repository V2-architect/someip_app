#!/bin/bash

sudo docker stop $(sudo docker ps | grep mn. | awk '{print $NF}')
