#!/usr/bin/python3
#Author     : Aiman
#Date       : 16:03:2021

# std lib
import sys

# custom lib
from revshell_list import reverse_shell_list
from revshell import reverse_shell

def help_me():
    print("Usage: petai.py [--help] [-r [REVERSE SHELL]] [-i [IP]] [-p [PORT]]")
    print("Exa: petai.py -r 1 -i 10.10.10.10 -p 9901")
    print("")
    print("OPTIONS:")
    print("-r <reverse_shell_id>:       Reverse Shell ID")
    print("-i <ip_address>:             Ip address")
    print("-p <port_for_listening>:     Port")
    print("")
    print("NICE OPTIONS:")
    print("--help:      show help")
    print("--list:      list all reverse shell [ID]")

def main():
    try:
        if sys.argv[1] == "--help":     #help
            help_me()
        elif sys.argv[1] == "--list":   #list
            reverse_shell_list()
        elif sys.argv[1] == "-r":       #reverse shell
            try:
                revshell = sys.argv[2]          #reverse shell id
                try: 
                    sys.argv[3] == "-i"     #ip address
                    try:
                        if sys.argv[5] == "-p":
                            user_ip = sys.argv[4]       #user input ip address
                            user_port = sys.argv[6]     #user input listening port
                            reverse_shell(revshell, user_ip, user_port)
                        else:
                            print("Missing An Arguments")
                    except:
                        print("Missing An Arguments")
                except:
                    print("Missing An Arguments")
            except:
                print("Missing an Arguments")
        else:
            print("Hmmmm It's seems wrong'")

    except:
        print("Usage: petai.py [--help] [Options] [Type]")
        print("")
        print("Error: Sorry, Try This '--help'")

if __name__ == "__main__":
    main()
