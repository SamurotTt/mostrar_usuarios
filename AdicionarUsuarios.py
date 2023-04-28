#!/usr/bin/env python3

import subprocess

#definindo uma variável para usuário e senha
novo_usuário = "Erico_limdo"
nova_senha = "banana1223"

#cria o usuário e senha no sistema Linux
subprocess.run(["sudo", "useradd", novo_usuário])
subprocess.run(["sudo", "passwd", novo_usuário], input=f"{nova_senha}\n{nova_senha}\n".encode())