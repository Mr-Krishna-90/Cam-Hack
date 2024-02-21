import os
import requests
import re
import colorama
import random
from requests.structures import CaseInsensitiveDict

colorama.init()


os.system("clear")

def banner():
    print("\033[93m")
    print("""
                         __________
                      .~#########%%;~.
                     /############%%;`\\
                    /######/~\\/~\\%%;,;,\\
                   |#######\\    /;;;;.,.|
                   |#########\\/%%%%;;.,.|
          XX       |##/~~\\####%;;;/~~\\;,|       XX
        XX..X      |#|  o  \\##%;/  o  |.|      X..XX
      XX.....X     |##\\____/##%;\\____/.,|     X.....XX
 XXXXX.....XX      \\#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \\######/%;\\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X'
X  \\...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
 X# \.X        @#%,.@   Cam-Hack v1.0      @#%,.@        
                @#%,.@              @#%,.@          
                  @#%,.@          @#%,.@            
                     @#%,.@      @#%,.@             
                       @#%.,@  @#%,.@              
                        Krishna Hackers
""")
    print(" ")
    print(" ")
    print("\033[92mX  \\...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx")
    print(" X# \.X        @#%,.@   Cam-Hack v1.0      @#%,.@        ")
    print("                @#%,.@              @#%,.@          ")
    print("                  @#%,.@          @#%,.@            ")
    print("                     @#%,.@      @#%,.@             ")
    print("                       @#%.,@  @#%,.@              ")
    print("                        Krishna Hackers")
    print(" ")
    print(" ")
    print("\033[91m                       ▶Coded by\033[92m Krishna \033[91m◀")
    print("\033[91m                      ⫸\033[93m  Krishna Hackers\033[91m ⫷")
    print(" ")
    print("\033[91m                    [Cam-Hack them with fun]")
    print(" ")
    print(" ")

def banner1():
    # Your banner1 code here
    pass

# Call the banner() function to display the information
banner()


url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

resp = requests.get(url, headers=headers)
data = resp.json()
countries = data['countries']

print("\033[1;31m\033[1;37m")


developer_name = "Krishna"
developer_channel_url = "https://t.me/+GrRkWxyiROs4ZGU1"
developer_instagram_id = "rach.itgamer999"

print("\033[1;37m")  # Set default text color

print(f"\033[1;36mDeveloper: \033[1;35m{developer_name}")
print(f"\033[1;36mDeveloper's Channel: \033[1;35m{developer_channel_url}")
print(f"\033[1;36mDeveloper's Instagram ID: \033[1;35m{developer_instagram_id}\n")


# About button
import time

def about():
    print("\033[91m")
    print("""
         ──▐─▌──▐─▌──
         ─▐▌─▐▌▐▌─▐▌─
         ─█▄▀▄██▄▀▄█─
         ──▄──██▌─▄──
         ▄▀─█▀██▀█─▀▄
         ▐▌▐▌─▐▌─▐▌▐▌
         ─▐─█────█─▌─
         ────▌──▐────
    """)
    print("\033[93m                  CALL ME \033[92mKrishna ")
    print("\033[93m             IAM FROM \033[92mDARK LEADER")
    print("\033[93m       IM A \033[92mGEEK\033[93m WITH LOTS OF EXCITEMENT")
    print("\033[93m             HOPE YOU LIKE THIS SCRIPT")
    print("\033[93m         OOPS... I TALK A LOT SRY FOR THAT ")
    print("\033[93m        Telegram Channel:\033[92m https://t.me/+GrRkWxyiROs4ZGU1\033[0m")
    print("\033[92m                BYEE..............")
    time.sleep(6.0)
    banner()
    menu()

def banner():
    # Your banner code here
    pass

def menu():
    # Your menu code here
    pass

# Call the about() function to display the information
about()

# Card view design with border and colorful developer information
def print_card(country_code, country_name, count):
    print("\033[1;37m┌" + "─" * 28 + "┐")
    print(f"\033[1;37m│\033[1;36m Country Code: {country_code:<8} \033[1;37m│")
    print(f"\033[1;37m│\033[1;35m Country Name: {country_name:<20} \033[1;37m│")
    print(f"\033[1;37m│\033[1;34m Count: {count:<27} \033[1;37m│")
    print(f"\033[1;37m│\033[1;32m Developer: {developer_name:<21} \033[1;37m│")
    print(f"\033[1;37m│\033[1;32m Channel: {developer_channel_url:<23} \033[1;37m│")
    print(f"\033[1;37m│\033[1;32m Instagram ID: {developer_instagram_id:<17} \033[1;37m│")
    print("\033[1;37m└" + "─" * 28 + "┘")

# Print card views for each country
for key, value in countries.items():
    print_card(key, value["country"], value["count"])

try:
    country = input("\033[1;37mCode(##) : ")
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
    
        with open(f'{country}.txt', 'w') as f:
            for ip in find_ip:
                print("")
                print("\033[1;31m", ip)
                f.write(f'{ip}\n')
except:
    pass
finally:
    print("\033[1;37m")
    print('\033[37mSave File :'+country+'.txt')

exit
