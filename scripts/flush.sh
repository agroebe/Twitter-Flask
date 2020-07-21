#!/bin/bash
image=$( docker ps --format '{{.Names}}' | findstr twitterflask_web_ )
echo $image
winpty docker exec -it $image python ../scripts/db/flush.py