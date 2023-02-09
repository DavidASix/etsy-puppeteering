from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def login(d):
    # Get Credentials
    c = open("private", "r").read().split()
    [u, p] = [c[0], c[1]]
    # Navigate to login page and fill out form
    d.get('https://www.etsy.com/signin')
    username = d.find_element(By.ID, 'join_neu_email_field')
    password = d.find_element(By.ID, 'join_neu_password_field')
    username.clear()
    password.clear()
    username.send_keys(u)
    password.send_keys(p)
    # Find and click login button
    submit = d.find_element(By.XPATH, "//*[@type='submit'][contains(@value, 'sign-in')]")
    submit.click()


def get_order_ids(d):
    # Navigate to shop manager
    shopManager = d.find_element(By.XPATH, "//a[label='Shop Manager']")
    shopManager.click()

    
    orderLink = d.find_element(By.XPATH, "//a[contains(@href, 'orders/sold')]")
    orderLink.click()

    ordersComplete = d.find_element(By.XPATH, "//a[contains(@href, 'orders/sold/completed')]")
    ordersComplete.click()

    elements = d.find_elements(By.XPATH, "//input[contains(@href, '?order_id')]")

    # Iterate through the elements and print their tag names
    for element in elements:
        print(element.tag_name)

def add_cookies(d):
    cs = open('cookies', 'r')
    lines = 0
    for cookie in cs:
        c = cookie.strip()
        c= c.split('=')
        d.add_cookie({'name': c[0], 'value': c[1]})
        lines += 1
    print('Added', lines/2, 'cookies')
    return d

def main():
    # Initialize the web browser
    driver = webdriver.Firefox()
    # Initially load a page to to avoid cookie aversion error
    driver.get('https://www.etsy.com')
    # Load Auth cookies
    driver = add_cookies(driver)
    # Navigate to orders page
    driver.get("https://www.etsy.com/your/orders/sold/completed")
    # Close the web browser
    #driver.quit()

main()


