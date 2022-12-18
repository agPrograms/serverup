# This is a small little program that checks if a server is up or down. I know I could have used simple requests to check if its operational, but I wanted to learn how to use subprocess.
# I also wanted to learn how to use Discord webhooks, so I added that in as well. I'm not sure if this is the best way to do it, but it works for me. 
# Use at your own risk. I'm not responsible for any damages caused by this program. Not that there should be any! It might not even work! :D
import requests as r
import subprocess
import time as t

global cn;cn = 0 # Is there a better way?
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
        global cn
        if s.srvfind(mc) == True and cn == 0:
            #global cn
            cn = 1
            s.srvup()
        elif cn==1: #doesnt need to here right?
            pass
        else:
            cn = 3
    
    def srvcheck():
        global cn
        srvcheck = s.srvfind(mc) # dont want to repeat myself, so storing it in a variable.
        if srvcheck == True and cn == 1:
            print('Server is STILL OR BACK up!') #really here for debugging.
            #global cn;cn = 1
            pass
        elif srvcheck == True and cn == 3:
            #global cn;cn=1
            cn = 1
            s.srvup()
        elif srvcheck == False and cn == 3:
            s.srvdown()
            print('Server is still down. Terminating program...');t.sleep(5);exit()
        elif srvcheck == False and cn == 1:
            cn=3

        else:
            #global cn
            cn = 3
            s.srvdown()

s.srvcatch()
while(cn==1): # I could make it check the task state like true here instead of the numbers... lol
    t.sleep(30)
    s.srvcheck()
#    if cn == 2:   # changed while loop to check variable instead of if statement
#        s.srvdown()
#        cn = 3
    #elif cn == 3: #rescue operation

while(cn==3): # I could make it check the task state like false here instead of the numbers... lol
    print('Is the server restarting? Checking in 10 seconds...')
    t.sleep(10)
    s.srvcheck()
#    if cn == 1:   # created while loop to check variable instead of if statement
#        s.srvup()
#        #cn = 2
#    else:
#        print('Server is still down. Terminating program...');t.sleep(5);exit() # diabolical~
