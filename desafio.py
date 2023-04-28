#!/usr/bin/env python3

import pwd, subprocess

novo_usuário = "Eric"
nova_senha = "banana1223"

subprocess.run(["sudo", "useradd", novo_usuário])
subprocess.run(["sudo", "passwd", novo_usuário], input=f"{nova_senha}\n{nova_senha}\n".encode())

for usuarios in pwd.getpwall():
    print(usuarios.pw_name)