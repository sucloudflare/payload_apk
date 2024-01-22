# Códigos de Cores ANSI
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def print_colored(text, color):
    print(f"{color}{text}{END}")

def print_banner_line():
    print("╔─────────────────────────────────────────────────────────╗")

def print_banner_footer():
    print("┖─────────────────────────────────────────────────────────┙\n")

def banner1():
    print_banner_line()
    print_colored(f"|    {RED}PAYLOAD APK{WHITE} -                                   |", WHITE)
    print_colored(f"|      Please do not upload APK to {RED}edsonbruno.kesug.com{WHITE}         |", WHITE)
    print_banner_footer()

    print_colored(f"{GREEN}                  .           .           ", WHITE)
    # ... restante do banner ...

    print_colored("                  MMMMM   MMMMM        PAYLOAD APK   v1.0   ", WHITE)
    print_colored("                  MMMMM   MMMMM        Written In Python3   ", WHITE)
    print_colored("                  MMMMM   MMMMM           ", WHITE)
    print_colored("                  MMMMM   MMMMM           ", WHITE)
    print_colored(f"                  .MMM.   .MMM.           {WHITE}\n", WHITE)
    print_banner_line()
    print_colored(f"| {WHITE}[ {RED}Author{WHITE}  ] {YELLOW}Pushpender Singh                             {WHITE}|", WHITE)
    print_colored(f"| [ {RED}GitHub{WHITE}  ] {YELLOW}https://github.com/sucloudflare/           {WHITE}|", WHITE)
    print_colored(f"| [ {RED}TikTok{WHITE} ] {YELLOW}tiktok.com/sucloudflare/ {WHITE}|", WHITE)
    print_banner_footer()

    print_banner_line()
    print_colored(f"|     {RED}DISCLAIMER : Legal                      {WHITE}| ", WHITE)
    print_banner_footer()

def banner2():
    print("""
              ^             """+RED+""" _____                            _    """+WHITE+"""
             | |            """+RED+"""|  __ \                          | |   """+WHITE+"""
           @#####@          """+RED+"""| |__) |___  __ _ _   _  ___  ___| |_  """+WHITE+"""
         (###   ###)-.      """+RED+"""|  _  // _ \/ _` | | | |/ _ \/ __| __| """+WHITE+"""
       .(###     ###) \     """+RED+"""| | \ \  __/ (_| | |_| |  __/\__ \ |_  """+WHITE+"""
      /  (###   ###)   )    """+RED+"""|_|  \_\___|\__, |\__,_|\___||___/\__| """+WHITE+"""
     (=-  .@#####@|_--"   +================"""+RED+"""| |"""+WHITE+"""========================+
     /\    \_|l|_/ (\     +  DON't Dare to """+RED+"""| |"""+WHITE+"""  Upload Infected APK   + 
    (=-\     |l|    /     +            TO  """+RED+"""|_|"""+WHITE+""" """+RED+""" VIRUSTOTAL """+WHITE+"""           +
     \  \.___|l|___/      +===========================================+
     /\      |_|   /    
    (=-\._________/\       ["""+RED+"""Author"""+WHITE+"""] """+GREEN+"""Pushpender Singh"""+WHITE+"""
     \             /       ["""+RED+"""GitHub"""+WHITE+"""] """+GREEN+"""github.com/PushpenderIndia"""+WHITE+"""
       \._________/       +===========================================+
         #  ----  #       +    Please Contribute To This Project      +
         #   __   #       +===========================================+
         \########/ """)
