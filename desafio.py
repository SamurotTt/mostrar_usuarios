#!/usr/bin/env python3

import pwd, subprocess

novo_usuario = "Eric"
nova_senha = "banana1223"

subprocess.run(["sudo", "useradd", novo_usuario])
subprocess.run(["sudo", "passwd", novo_usuario], input=f"{nova_senha}\n{nova_senha}\n".encode())

for usuarios in pwd.getpwall():
    print(usuarios.pw_name)
