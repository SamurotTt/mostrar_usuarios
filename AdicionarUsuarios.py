#!/usr/bin/env python3

import subprocess

#definindo uma variável para usuário e senha
novo_usuario = "Erico_limdo"
nova_senha = "banana1223"

#cria o usuário e senha no sistema Linux
subprocess.run(["sudo", "useradd", novo_usuario])
subprocess.run(["sudo", "passwd", novo_usuario], input=f"{nova_senha}\n{nova_senha}\n".encode())
