#!/bin/bash
# ara hacer esto, primero tendríamos que solicitar los encabezados de una respuesta y luego extraer el código de respuesta. Así es como se vería.
curl -sX GET "$1" -L 200
