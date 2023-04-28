#!/usr/bin/env python3

import pwd

#lista todos os usuários do linux

for usuarios in pwd.getpwall():
    print(usuarios.pw_name)