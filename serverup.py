# This is a small little program that checks if a server is up or down. I know I could have used simple requests to check if its operational, but I wanted to learn how to use subprocess.
# I also wanted to learn how to use Discord webhooks, so I added that in as well. I'm not sure if this is the best way to do it, but it works for me. 
# Use at your own risk. I'm not responsible for any damages caused by this program. Not that there should be any! It might not even work! :D
import requests as r
import subprocess
import time as t

import requests as r
import subprocess
import time as t

mc = "java.exe" # Is there a better way?
webhook_url = "YOUR WEBHOOK HERE"

class s:
    def srvup():
        print('Server is up! Sending message to Discord...')
        global dataUP
        dataUP = {
            "content": "The Minecraft Server is up! 😍"
        }
        r.post(webhook_url, json=dataUP)

    def srvdown():
        print('Server is down! Sending message to Discord...')
        global dataDOWN
        dataDOWN = {
            "content": "The Minecraft Server is down! 😒"
        }
        r.post(webhook_url, json=dataDOWN)

    def srvfind(game_name):
        call = 'TASKLIST', '/FI', 'imagename eq %s' % game_name
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[-1]
        return last_line.lower().startswith(game_name.lower())

    def srvcatch():
        srvcat1 = s.srvfind(mc)
        if srvcat1 == True:
            s.srvup()
        else:
            pass
    def srvch(mc):
        srvcat2 = s.srvfind(mc)
        if srvcat2 != True:
            global x;x=0
            while(s.srvfind(mc)!=True) and x<3:
                x+=1
                print('Server is down! Restarting? Check in 5 seconds...')
                t.sleep(5)
            if (s.srvfind(mc)==True):
                x = x-3
                s.srvup()
            elif(x==3):
                s.srvdown()
                print('Server is still down. Terminating program...');t.sleep(5);exit()
        else:
            pass


s.srvcatch()
srvchecking = s.srvch(mc)
while(srvchecking == True):
    print('Server is up!')
    t.sleep(20)

while(srvchecking == False):
    print('Server is down!')
    t.sleep(20)
