import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_websites(website_list):
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'
    
    with open(host_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website not in content:
                file.write(f"{redirect} {website}\n")
                print(f"Blocked {website}")
            else:
                print(f"{website} already blocked")

def unblock_websites(website_list):
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(host_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

def main():
    if not is_admin():
        print("This script requires admin privileges. Restarting with admin rights...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    current_time = datetime.datetime.now().strftime("%H:%M")
    Stop_time = input("Enter stop time (HH:MM): ").strip()
    
    try:
        current_time_obj = datetime.datetime.strptime(current_time, "%H:%M")
        Stop_time_obj = datetime.datetime.strptime(Stop_time, "%H:%M")
        
        # Calculate the Focus Time
        Focus_Time = Stop_time_obj - current_time_obj
        Focus_Time_in_minutes = Focus_Time.total_seconds() / 60
        print(f"Focus Time: {Focus_Time_in_minutes} minutes")

        website_list = ["www.facebook.com", "facebook.com"]

        if current_time_obj < Stop_time_obj:
            block_websites(website_list)
            print("Focus Mode is ON!")
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M")
                current_time_obj = datetime.datetime.strptime(current_time, "%H:%M")
                if current_time_obj >= Stop_time_obj:
                    unblock_websites(website_list)
                    print("Focus Mode is OFF!")
                    break
                time.sleep(30)
        else:
            print("Current time is already past the stop time. Focus mode cannot be enabled.")
    
    except ValueError as e:
        print(f"Error: Invalid time format. Please use HH:MM format. {e}")

if __name__ == "__main__":
    main()
