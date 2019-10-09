from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import getpass

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
browser = webdriver.Chrome('/home/pratik/Documents/chromedriver', chrome_options=options)

browser.get("https://facebook.com/")

phone='7780813063'
password=getpass.getpass("Password: ")

userid_field=browser.find_element_by_id('email')
userid_field.send_keys(phone)

password_field=browser.find_element_by_id('pass')
password_field.send_keys(password)

browser.find_element_by_id('loginbutton').click()	

print ("Successfully Logged in")

# url=browser.current_url()

message_count=browser.find_element_by_id('mercurymessagesCountValue').text
print message_count
if message_count =="":
	print "No New Messages."
else:
	print "Yes, New Messages."

browser.close()