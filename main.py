from instagrapi import Client
import os
import time
from colorama import Fore, Style, Back ,init

USERNAME = ""
PASSWORD = ""

cl = Client()
SESSION_FILE_PATH = os.path.expanduser("~/instabot/session.json") # Your File Path
init()

try:
    cl.load_settings(SESSION_FILE_PATH)
    cl.login(USERNAME, PASSWORD)
    print(Fore.GREEN + "[+] Successfully Loged In With Session")
except Exception:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE_PATH)
    print(Fore.RED + "[-] New Login + Session Created")
print(Fore.WHITE + f"User ID: {cl.user_id}")

def menu():
    os.system("clear || cls")
    print(Fore.RED + r"    ______                                          ")
    print(Fore.RED + r"   / ,__      ____ __ _        _____     __         ")
    print(Fore.RED + r"  / /_( ) __ /  \   /_ _____  / _ \ __  / /_        ")
    print(Fore.LIGHTYELLOW_EX + r" / / / / __ \\ \/  __/ _  \  / _  / _ \/ __/        ")
    print(Fore.WHITE + r"/_/ /_/_/ /_,__/__/  \__,\_\/___ /\___/_/__________ ")
    print(" ")
    print(Fore.GREEN + "# Originally Coded By Mallrs")
    print(" ")
    print(Fore.YELLOW + "[1] Scan User   [2] Send DM   [3] Exit   ")
    init()

def ScanUser():
    os.system("clear || cls")
    target = input(Fore.RED + "Enter Username "+Fore.LIGHTBLACK_EX+"> ")
    print(Fore.GREEN + "Scanning...")
    try:
        user = cl.user_info_by_username_v1(target)
        os.system("clear || cls")
        print(Fore.YELLOW + "============ Account Info ============")
        print(Fore.WHITE + "["+Fore.GREEN+"*"+Fore.WHITE + "] ID : " + Fore.GREEN + f"{user.pk}")
        print(Fore.WHITE + "["+Fore.GREEN+"*"+Fore.WHITE + "] Username : " + Fore.GREEN + f"{user.username}")
        print(Fore.WHITE + "["+Fore.GREEN+"*"+Fore.WHITE + "] Full Name : " + Fore.GREEN + f"{user.full_name}")
        print(Fore.WHITE + "["+Fore.GREEN+"*"+Fore.WHITE + "] Followers : " + Fore.GREEN + f"{user.follower_count}")
        print(Fore.WHITE + "["+Fore.GREEN+"*"+Fore.WHITE + "] Following : " + Fore.GREEN + f"{user.following_count}")
        print(Fore.WHITE + "["+Fore.GREEN+"*"+Fore.WHITE + "] Bio : " + Fore.GREEN + f"{user.biography}")

    except Exception as e:
        print(Fore.RED + f"[-] An Error Occured While Getting User Info:")

    input(Fore.RED+"\nPress Enter to return to menu...")

def SendDM():
    os.system("clear || cls")
    target = input(Fore.RED + "Enter Username "+Fore.LIGHTBLACK_EX+"> ")
    count = int(input(Fore.RED + "Enter Nummber Of DM "+Fore.LIGHTBLACK_EX+"> "))
    msg = input(Fore.RED + "Enter Message "+Fore.LIGHTBLACK_EX+"> ")
    i=0
    try:
        user = cl.user_info_by_username_v1(target)
        user_id = user.pk        
        print(Fore.GREEN + f"[+] Target User ID: {user_id}")
    except:
        print(Fore.RED + f"[-] Failed to get user ID: {e}")
        input("Press Enter...")
        return

    for i in range(count):
        try:
            cl.direct_send(msg, [user_id])
            print(Fore.GREEN + f"[+] DM Sent ({i+1}/{count})")
        except Exception as e:
            print(Fore.RED + f"[-] Error while sending DM: {e}")
            break

    input(Fore.YELLOW + "\nPress Enter to return to menu...")

def main():
    while True:
        menu()
        user_selection = input(Fore.RED + "> ")
        if user_selection == "1":
            ScanUser()
        elif user_selection == "2":
            SendDM()
        elif user_selection == "3":
            print(Fore.GREEN + "Exiting...")
            break
        else:
            print(Fore.RED + "[-] Invalid selection!")
            input(Fore.YELLOW + "Press Enter to continue...")

if __name__ == "__main__":
    main()
