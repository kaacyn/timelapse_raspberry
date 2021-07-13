#!/bin/sh
path_imagem_origem=$(awk -F "=" '/path_imagem_origem/ {print $2}' config.ini)

DATE=$(date +"%Y-%m-%d_%H-%M")

raspistill -o ${path_imagem_origem}/$DATE.png
