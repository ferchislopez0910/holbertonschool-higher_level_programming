#!/bin/bash
# Este comando lo que hace es
# I es para mostrar solo encabezados -s corregir errores
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
