# Time Lapse Raspberry
## Um simples script de time lapse para raspberry

Este é um script que criei e estou aprimorando para fazer time lapse de todo o crescimento de umas plantas que cultivo em casa. O que está aqui é praticamente uma cópia da versão que uso em produção. Fique a vontade para usar e sugerir novas melhorias.

- Tira fotos com a câmera interna do raspberry.
- Faz upload para uma conta de ftp

## Instalação

Você vai precisar baixar esse script em seu raspberry dentro de um diretorio.
Para agilizar a configuração use o seguinte caminho de pastas em seu raspberry:
```sh
mkdir /home/pi/Scripts/timelapse_raspberry
```
Renomeie o arquivo config.exemple.ini para config.ini:
```sh
mv config.exemple.ini mv config.ini
```
Abra e edite conforme sua necessidade:
```sh
nano config.ini
```

Configure no seu crontab(com o comando crontab -e) as seguintes tarefas:
```sh
# Tira foto a cada 15 minutos
*/15 * * * * cd  /home/pi/Scripts/timelapse_raspberry && ./tirafoto.sh > /dev/null 2>&1

# Faz upload da foto a cada 10 minutos
*/10 * * * * cd /home/pi/Scripts/timelapse_raspberry && python upload.py > /dev/null 2>&1
```

# Configuracão interface(ip fixo)
Se quiser acessar o seu raspberry sempre remotamente, então o ideal é configurar um IP fixo:
```sh
sudo nano  /etc/dhcpcd.conf 
```
Configure a interface 'wlan0' se estiver usando rede sem fio.
```sh
interface wlan0
static ip_address=192.168.0.30
#static ip6_address=fd51:42f8:caae:d92e::ff/64
static routers=192.168.0.1
#static domain_name_servers=192.168.0.1 8.8.8.8 fd51:42f8:caae:d92e::1
```

Por enquanto é só :-)!
