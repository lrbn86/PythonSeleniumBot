# A bot that uses a referral link, creates a random account, and then 
# completes with one of the entries (e.g. visit FB page)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import string

# Generate random string with given length or default length of 10
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


# Open Firefox with given link
driver = webdriver.Firefox()
driver.get("https://gleam.io/cookiefix?sa=https://gleam.io/8IFue/win-a-heckler-and-koch-sp5-pistol-w-binary-trigger%3Fl%3Dhttps%253A%252F%252Fwww.classicfirearms.com%252Fcontest%252Fwin-a-hk-sp5-pistol-binary-trigger%252F%253Fgsr%253D8IFue-u2N6sON14a%26r%3D%26gsr%3D8IFue-u2N6sON14a")

def repeatProcess():
    main_window = driver.current_window_handle
    time.sleep(5)
    # Click on Visit Facebook
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/a").click()
    # Then actually visit facebook page
    driver.switch_to.window(main_window)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div[2]/div/a").click()
    full_name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[1]/label/div[2]/input")
    email = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[2]/label/div[2]/input")
    dob = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[3]/div/label/div[2]/input")
    save_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div/span[1]/button")
    full_name.send_keys("Bob")
    email.send_keys(randomString() + "@gmail.com")
    dob.send_keys('01291972')
    time.sleep(5)
    save_btn.click()
    logout_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/span/div[1]/div[2]/a[2]")
    logout_btn.click()
    time.sleep(5)
 

print("Initial trial")
# Do this once and then repeat process without opening new tab to FB
main_window = driver.current_window_handle
time.sleep(5)
# Click on Visit Facebook
print("Just opened a window [" + driver.title + "].")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/a").click()

# Then actually visit facebook page
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div[1]/div[2]/a").click()
driver.switch_to.window(main_window)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div[2]/div/a").click()

full_name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[1]/label/div[2]/input")
email = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[2]/label/div[2]/input")
dob = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/fieldset[2]/div[2]/div/div/div[3]/div/label/div[2]/input")
save_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/div[12]/div/div/form/div/span[1]/button")

full_name.send_keys("Bob")
email.send_keys(randomString() + "@gmail.com")
dob.send_keys('01291972')
time.sleep(5)
save_btn.click()

logout_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div[6]/div[2]/div[3]/div/span/div[1]/div[2]/a[2]")
logout_btn.click()
time.sleep(5)


# Repeat for this n times
i = 0
n = 5
print("Repeating for " + n + "times.")
while i < n:
    print("Repeating process...")
    repeatProcess()
    i += 1

driver.quit()
print("Complete.")
