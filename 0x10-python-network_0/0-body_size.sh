#!/bin/bash
# Este comando lo que hace es 
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
