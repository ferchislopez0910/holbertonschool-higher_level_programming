#!/bin/bash
# Este comando lo que hace es 
curl -sI $1 | grep Content-Length | cut -d " " -f 2
