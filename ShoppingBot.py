from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import info

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#3080 card from bestbuy
test = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956SS'
driver.get(test)

#the purchase is not completed yet
Purchased = False 

#this starts the process of the purchase
while not Purchased:
    
    try:
    	#this creates a button to click by selcting through classm, even the button is sold out
        atcBtn = WebDriverWait(driver, 10).until(EC.precence_of_element_located((By.CSS_SELECTOR, ".fulfillment-add-to-cart-button")))
        #click method will click the button atcBtn.
        atcBtn.click()
        
    except:
    	#the error is usually not available. Trying to make it only shows up for once in the terminal
        print("item might be sold out. Keep refreshing until it is available")
        #restart the process
        driver.refresh()
        continue
    
    print("adding item to cart")
    
    try:
        
        #get method to enter the cart page    
        driver.get("https://www.bestbuy.com/cart")

        #create a check out botton by using xpath, filtering the word checkout.
        ChkBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Checkout')]")))
        #click the check out botton
        ChkBtn.click()

        #locating the emailfield by searching the id tag
        emailField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'fld-e')))
        #sends the infomation to the emailfield
        emailField.send_keys(info.email)

        #locating the pwfield by searchign the id tag
        pwField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fld-p1")))
        #send the pw to the pwfield
        pwField.send_keys(info.password)

        #create a signin button by locating the signin button of the website by using xpath	
        signInBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In' )]")))
        #click the button to sign in
        signInBtn.click()
        print("Signing in")

        #locating the cvvField on the webpage by searching its id
        cvvField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cvv")))
        #sends the cvv info the cvvfield
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        #create the place order button by locating the place order botton on webpage using css_selector of the class
        placeOrderBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track")))
        #placeOrderBtn.click()
        print("order placed")
      	Purchased = True
    
    #this will rerun the the script when some unexpected error occurrs
    except:
        driver.get(test)
        print("Error - restarting bot")
        continue

print("cash money")
