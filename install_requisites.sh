#!/bin/bash

echo "Iniciando instalación de dependencias para el proyecto 'GestionClientes'..."

# Actualizar lista de paquetes
echo "Actualizando paquetes del sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar Python 3 y pip
echo "Instalando Python 3 y pip..."
sudo apt install -y python3 python3-pip

# Instalar MySQL Server
echo "Instalando MySQL Server..."
sudo apt install -y mysql-server

# Iniciar y habilitar MySQL
echo "Habilitando e iniciando el servicio MySQL..."
sudo systemctl enable --now mysql

# Instalar conector de Python para MySQL
echo "Instalando mysql-connector-python..."
pip3 install mysql-connector-python

# Confirmación final
echo "Instalación completada correctamente."
echo "Puedes ejecutar el proyecto con: python3 gestion_clientes.py"
