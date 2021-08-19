#!/bin/bash
# Este comando lo que hace es 
curl -I $1 | grep Content-Length | cut -d " " -f 2
