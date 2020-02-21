from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import names
import string
import random

def generate3RandomNumbers():
    ans = ""
    m = [1,2,3,4,5,6,7,8,9,10]
    for i in range(3):
        ans += str(random.choice(m))
    return ans

def generateRandomName():
    return names.get_full_name()

def generateRandomEmail(strlen=10):
    letters = string.ascii_lowercase
    emails = ["@gmail.com", "@hotmail.com",  "@yahoo.com"];
    return ''.join(random.choice(letters) for i in range(strlen)) + generate3RandomNumbers()  + random.choice(emails)

def generateRandomDOB():
    month_num = [1,2,3,4,5,6,7,8,9,10,11,12]
    m_digit_year = [7,8]
    last_digit_year = [2,3,4,5,6,7,8,9]
    day_num = ['01','02','03','04','05','06','07','08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    return '0' + str(random.choice(month_num)) + str(random.choice(day_num)) + '19' + str(random.choice(m_digit_year)) + str(random.choice(last_digit_year))

def startBot():

    # Generate random information to fill in the input fields
    name = generateRandomName()
    email = generateRandomEmail()
    dob = generateRandomDOB()
    
    i = 0
    repeats = int(input("How many referrals? "))
    print("Starting program ...")

    # This is the link that we want to open in a new window
    TARGET_URL = "https://gleam.io/cookiefix?sa=https://gleam.io/8IFue/win-a-heckler-and-koch-sp5-pistol-w-binary-trigger%3Fl%3Dhttps%253A%252F%252Fwww.classicfirearms.com%252Fcontest%252Fwin-a-hk-sp5-pistol-binary-trigger%252F%253Fgsr%253D8IFue-u2N6sON14a%26r%3D%26gsr%3D8IFue-u2N6sON14a"
    
    # We will use Firefox web browser
    browser = webdriver.Firefox()
    while i < repeats:

        browser.get(TARGET_URL) # Open a new window with the given link
        
        time.sleep(5) # Wait for a bit for the site is load
        
        # Click on Visit Facebook Link
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/a").click()
        
        # Visit Facebook page
        
        # Sometimes, the visit to the actual facebook page does not show up, so we need to check
        # whether that link exists. If it doesn't, then we just hit continue, otherwise we hit the facebook link
        actualFB_link = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div[1]/div[2]/a")
        if actualFB_link.is_displayed():
            actualFB_link.click()
        else:
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div[2]/div/a").click()
        
        # Close Facebook page
        browser.switch_to.window(browser.window_handles[0])
        
        # We will close FB page only if it was opened in a new tab
        if len(browser.window_handles) > 1:
            browser.switch_to.window(browser.window_handles[1])
            browser.close()
            browser.switch_to.window(browser.window_handles[0])    
            continue_btn = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div[2]/div/a")
            continue_btn.click()
       
        # Get all the input fields
        full_name_input = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[1]/label/div[2]/input")
        email_input = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[2]/label/div[2]/input")
        dob_input = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[3]/div/label/div[2]/input")
        save_btn = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div/span[1]/button")
        
        # Fill in all the input fields
        full_name_input.send_keys(name)
        email_input.send_keys(email)
        dob_input.send_keys(dob)
        time.sleep(3) # Give the button a chance to turn to green so that it's clickable
        save_btn.click()
        
        # Log out
        logout_btn = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/span/div[1]/div[2]/a[2]")
        logout_btn.click()

        # Open new tab
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[0])    
        # Close prev tab and focus on first tab
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        
        i += 1
        print("Completed a referral ...")
    browser.quit() # When we complete the while loop, terminate program
startBot()
print("Program Terminated.")
