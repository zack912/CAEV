#!/bin/bash
rm -r /home/zack/CAEV/apps/cat/consumo_promedio/migrations/000*
rm -r /home/zack/CAEV/apps/cat/diametro_toma/migrations/000*
rm -r /home/zack/CAEV/apps/cat/marca_medidor/migrations/000*
rm -r /home/zack/CAEV/apps/cat/tipo_servicio/migrations/000*
rm -r /home/zack/CAEV/apps/cat/tipo_usuario/migrations/000*
rm -r /home/zack/CAEV/apps/cat/ubicacion_toma/migrations/000*
rm -r /home/zack/CAEV/apps/cliente/migrations/000*
rm -r /home/zack/CAEV/apps/empleado/migrations/000*
rm -r /home/zack/CAEV/apps/pagos/migrations/000*

echo "se ha eliminado correctamente = ) "
zenity --info --title "Hola venudo" --text "Autodestruccion del proyecto en 3...2...1 te has jodido"