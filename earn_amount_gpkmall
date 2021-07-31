import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import mysql.connector as connector
from tqdm import tqdm
from colorama import Fore, Style
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



start_time = datetime.now()

mobile_emulation = {

   "deviceMetrics": { "width": 360, "height": 600, "pixelRatio": 3.0 },

   "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" 
   }

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument('headless')

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options = chrome_options)
driver.get('https://www.gbkmall.in/Web/en/LogReg.aspx')

def execute(user,pwd):

	wait = WebDriverWait(driver,20)
	wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="username1"]')))

	#login
	username = driver.find_element_by_xpath('//*[@id="username1"]')
	username.send_keys(user)
	password = driver.find_element_by_xpath('//*[@id="pwd1"]')
	password.send_keys(pwd)
	login_button=driver.find_element_by_xpath('//*[@id="btnRegister1"]')
	login_button.click()

	wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[16]/div[3]')))

	#AD
	ad_close_button = driver.find_element_by_xpath('/html/body/div[16]/div[3]')
	ad_close_button.click()

	wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[11]/div[2]/ul/li[1]')))

	#lazad
	lazad = driver.find_element_by_xpath('/html/body/div[11]/div[2]/ul/li[1]')
	lazad.click()

	wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]')))

	count_label = driver.find_element_by_xpath('//*[@id="lblTotalNum"]')

	count = int(count_label.text)
	print (Fore.BLUE + "[+] Finished Number of Orders : " +str(count)+Fore.LIGHTGREEN_EX)
	for i in tqdm(range(count+1,31),desc="Progress : "):

		send_order_button = driver.find_element_by_xpath('/html/body/div[4]')
		send_order_button.click()

		wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/div[3]/div[2]')))

		submit_button = driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[3]/div[2]')
		submit_button.click()

		while 1:
			try:
				alert = Alert(driver)
				alert.accept()
				break
			except KeyboardInterrupt:
				exit()
			except:
				pass
		time.sleep(2)

	user_log=driver.find_element_by_xpath('/html/body/footer/div/div[5]')
	user_log.click()

	wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/header/div/div[2]')))

	logout_button=driver.find_element_by_xpath('/html/body/header/div/div[2]')
	logout_button.click()



def get_username():
	mydb = connector.connect(host='localhost',user='',password='',database='test')
	mycursor = mydb.cursor()
	mycursor.execute('select userid, password from gpkmail;')
	myresult = mycursor.fetchall()
	for i in myresult:
		print (Fore.RED + '[+] Username : '+ Fore.LIGHTYELLOW_EX + i[0])
		print (Fore.RED + '[+] Password : '+ Fore.LIGHTYELLOW_EX + i[1])
		execute(i[0],i[1])



get_username()
driver.close()
driver.quit()
print (Style.RESET_ALL)
print ('[+] Execution time'+str(datetime.now()-start_time))
