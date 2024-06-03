from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import csv

# Configure your login credentials
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Initialize the WebDriver
driver = webdriver.Chrome()

def login():
    try:
        driver.get('https://example.com/login')
        
        # Find the username and password fields and enter the credentials
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        
        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        
        # Find and click the login button
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        
        # Wait for the login to complete
        time.sleep(5)  # Adjust based on your internet speed
        
        # Check if login was successful
        if "dashboard" in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed! Please check your credentials or CAPTCHA.")
            driver.quit()
            return False
        return True
    except NoSuchElementException as e:
        print(f"An error occurred during login: {e}")
        driver.quit()
        return False

if login():
    try:
        # Navigate to the target page (e.g., user profiles page)
        driver.get('https://example.com/user-profiles')

        # Extract data (this is a placeholder, adjust selectors as needed)
        profiles = driver.find_elements(By.CLASS_NAME, 'profile')
        
        # Prepare CSV file
        with open('user_profiles.csv', 'w', newline='') as csvfile:
            fieldnames = ['Username', 'Name', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for profile in profiles:
                username = profile.find_element(By.CLASS_NAME, 'username').text
                name = profile.find_element(By.CLASS_NAME, 'name').text
                email = profile.find_element(By.CLASS_NAME, 'email').text
                writer.writerow({'Username': username, 'Name': name, 'Email': email})

        print("Data extraction successful! Check user_profiles.csv")
        
    except NoSuchElementException as e:
        print(f"An error occurred during data extraction: {e}")
    finally:
        driver.quit()
else:
    print("Script terminated due to login failure.")
