#www.github/D34D-5H07
from os import system, name 
import rpc
import time
from time import mktime,sleep
def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
        
clear()
print("Connecting to Server_Name")
sleep(1)
clear()
print("Deadshot")
sleep(1.5)
clear()
client_id = '1234567890' # Enter YOur Client ID 
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) 
print("RPC connection successful.")
sleep(1)
clear()
print("RPC Running <--> Press CTRL+C To Stop")
time.sleep(1) #the time to start presenting
start_time = mktime(time.localtime())
while True:
    activity = {
            "details": "Deadshot",  
            "timestamps": {
                "start": start_time 
            },
            "assets": {
                "small_text": "text1",  # Edit as You Like
                "small_image": "image_name",  # must be the same image key 
                "large_text": "text2",  # anything you like
                "large_image": "image_name2"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
