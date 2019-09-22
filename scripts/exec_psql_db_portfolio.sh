#!/bin/bash

docker exec -it "postgis" psql -h localhost -U docker -p 5432 -d portfolio