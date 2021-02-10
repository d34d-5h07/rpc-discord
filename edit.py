#coded by deadshot
#www.github/D34D-5H07
from os import system, name 
import rpc
import time
from time import mktime,sleep
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
clear()
print("Connecting to Alvara")
sleep(1)
clear()
print("Coded By Deadshot")
sleep(1.5)
clear()
client_id = '809115126581166143'
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) 
print("RPC connection successful.")
sleep(1)
clear()
print("RPC Running <--> Press CNTRL+C To Stop")
time.sleep(1) #the time to start presenting
start_time = mktime(time.localtime())
while True:
    activity = {
            "details": "Ark Survival Evolved ",  
            "timestamps": {
                "start": start_time 
            },
            "assets": {
                "small_text": "Ark Survival Mobile",  # Edit as You Like
                "small_image": "ark_logo",  # must be the same image key 
                "large_text": "Alvara OutKast PVE ANZ",  # anything you like
                "large_image": "alvara1"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
