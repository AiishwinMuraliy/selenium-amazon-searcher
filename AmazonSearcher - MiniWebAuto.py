from selenium import webdriver
import time

# Intro Sequence
print('\n')
print("Hello! Welcome to Automated Amazon searcher!")
# Asking the user what to search
user_search = str(input("What would you like to search: "))

# Animation to bring up webpage
#print("Activating Bot..")
#time.sleep(4)
print("Launch!")
#time.sleep(1)


# Launcing the browser
PATH = "/Users/aiishwinmuraliy/WebDrivers/chromedriver" # Setting the path to the chromedriver
driver = webdriver.Chrome(PATH)
driver.get('https://www.amazon.ca/') # Opening Amazon

searchbox = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input') # Finding the searchbox
searchbox.send_keys(user_search) # Sending keys into the searchbob
searchbox.submit() # Pressing enter/return 