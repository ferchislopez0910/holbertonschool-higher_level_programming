#!/bin/bash
# ara hacer esto, primero tendríamos que solicitar los encabezados 
# de una respuesta y luego extraer el código de respuesta. Así es como se vería.
curl $1 -I -o headers | head -n 1 | cut '-d ' '-f2'