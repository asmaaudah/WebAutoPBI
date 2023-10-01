from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Menjalankan Web Browser
browser = webdriver.Chrome()

# Membuka Website Jubelio
browser.get('https://app.jubelio.com/login')

# Interaksi Otomatis
# Email dan Password
email = "qa.rakamin.jubelio@gmail.com"
password = "Jubelio123!"

# find username/email field and send the username itself to the input field
browser.find_element("name", "email").send_keys(email)
# find password input field and insert password as well
browser.find_element("name", "password").send_keys(password)
# click login button
browser.find_element("css selector",".btn-primary").click()

# wait the ready state to be complete
WebDriverWait(driver=browser, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
# <div role="alert" class="app-alert alert alert-danger alert-dismissable"><button type="button" class="close"><span aria-hidden="true">×</span><span class="sr-only">Close alert</span></button><li>Password harus diisi.</li></div>
# <div role="alert" class="app-alert alert alert-danger alert-dismissable"><button type="button" class="close"><span aria-hidden="true">×</span><span class="sr-only">Close alert</span></button><li>Format Email tidak valid.</li></div>
error_message = "Format Email tidak valid." 
error1 = "Password harus diisi."
# get the errors (if there are)
errors = browser.find_elements("css selector", ".alert-danger")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message or error1 in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
# close the driver
browser.close()