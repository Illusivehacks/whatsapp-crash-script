import os
import sys
import io
import time
import colorama
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set the default encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

colorama.init(autoreset=True)

R = colorama.Fore.RED
G = colorama.Fore.GREEN
C = colorama.Fore.CYAN
Y = colorama.Fore.YELLOW
M = colorama.Fore.MAGENTA
W = colorama.Fore.WHITE

logo = f"""{R}
██╗██╗     ██╗     ██╗   ██╗███████╗██╗██╗   ██╗███████╗
██║██║     ██║     ██║   ██║██╔════╝██║██║   ██║██╔════╝
██║██║     ██║     ██║   ██║███████╗██║██║   ██║███████╗
██║██║     ██║     ██║   ██║╚════██║██║██║   ██║██     ║
██║███████╗███████╗╚██████╔╝███████║██║╚██████╔╝███████║
╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚══════╝
{colorama.Style.RESET_ALL}"""

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-like
        os.system('clear')

def main():
    clear_screen()
    print(logo)
    print()

    try:
        cncode = int(input(f'{G}[{Y}+{G}]{M} Enter Country Code Without "+" eg.91 {C}=> '))
    except ValueError:
        print(f'{R}Invalid input. Please enter a numeric country code.')
        return main()

    print()
    num = input(f"{G}[{Y}+{G}]{M} Enter the Victim's Phone number\n\n{C}=> {cncode}  ")
    print()
    try:
        crash = int(input(f'{G}[{Y}+{G}]{M} Enter the number of crashes {W}(Max 15 per 30min) \n\n{C}=> '))
        if crash > 15:
            print(f'{R}Crash limit exceeded. Please enter a number less than or equal to 15.')
            return main()
    except ValueError:
        print(f'{R}Invalid input. Please enter a numeric value for crashes.')
        return main()

    combnum = f"+{cncode}{num}"
    print()
    Finalcall = input(f'{G}[?]{W} Do You Want To Change NO.{W}{combnum} {R}(Y/N)\n\n{C}=> ')
    
    if Finalcall.lower() == 'y':
        return main()
    
    clear_screen()
    print(f"{G}[{Y}+{G}]{M} Crashing Whatsapp on No. : {combnum} ...")
    time.sleep(5)

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={combnum}&text=Hello")

        # Wait until the message box is loaded
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]'))
        )
        
        # Click the send button multiple times
        for i in range(crash):
            driver.find_element(By.XPATH, '//span[@data-icon="send"]').click()
            time.sleep(2)  # Add a small delay between sends
        
    except Exception as e:
        print(f"{R}An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
