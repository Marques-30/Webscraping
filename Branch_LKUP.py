import time
import cx_Oracle
import csv
import subprocess
from urllib import quote
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import getpass
import requests
from BeautifulSoup import BeautifulSoup
import urllib2

LanID=raw_input("Lan-ID / Username: ")
Database=raw_input("Enter Orcale Database: ")
password=getpass.getpass("Enter Password: ")
ID = raw_input("Enter Schema Name: ")
table= raw_input("Enter Table Name: ")

###SQL Database Extract																																									
connection = cx_Oracle.connect(LanID+'/'+password+'@'+Database.upper())
cursor = connection.cursor()
with open("Branch_Zip.csv", 'w') as out_file:
        writer=csv.writer(out_file, lineterminator='\n')
        query = """SELECT * FROM {0}.{1}""".format(ID, table)
    	cursor.execute(query)
    	for row in cursor:
		    writer.writerow(row)
cursor.close()

wb = open('Branch_Zip.csv', 'r')
stripped = (line.strip() for line in wb)
count = 1
while count < 9:
	for rowNo, row in enumerate(wb):
		if (rowNo >0 and rowNo <=62):
	        	col=row.split(",")
	        	if rowNo in range(1, 30):
	        		query=col[4]
	        		print col[4]

#Bank site
driver=webdriver.Ie("C:\Users\Butilm01\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
driver.get('http://www.usbanklocations.com/bank-of-the-west-locations.htm')
time.sleep(30)
url = 'http://www.espnfc.com/spi/rankings/_/view/fifa/teamId/203/mexico?cc=5901'
page = urllib2.urlopen(url)
print count + " succeed, beginning data scrap."
soup = BeautifulSoup(page.read())
rank = soup.find("div", {"class": "rank-box"}).h6.contents
teaminfo = soup.find("div", {"class": "team-info"})
name = teaminfo.h4.contents
rating = teaminfo.ul.p.span.contents
print type(soup)

count = 1
while count < 10:
	if count <=9:
		driver=webdriver.Ie("C:\Users\Butilm01\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
		driver.get('http://www.usbanklocations.com/bank-of-the-west-locations_'+str(count)+'.htm')
		time.sleep(30)
		url = 'http://www.espnfc.com/spi/rankings/_/view/fifa/teamId/203/mexico?cc=5901'
		page = urllib2.urlopen(url)
		print count + " succeed, beginning data scrap."
		soup = BeautifulSoup(page.read())
		print type(soup)
		res = soup.findAll("article", {"class": "listingItem"})
		for r in res:
		    print("Company Name: " + r.find('a').text)
		    print("Address: " + r.find("div", {'class': 'address'}).text)
		    print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)
		print "Data retrieved and stored in document"
		count += 1
	else:
		break
		driver.quit()		

count = 10
while count < 20:
	if count <19:
		driver=webdriver.Ie("C:\Users\Butilm01\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
		driver.get('http://www.usbanklocations.com/bank-of-the-west-locations_'+str(count)+'.htm')
		time.sleep(30)
		print count + " succeed, begin data scrap."
		soup = BeautifulSoup(html, "lxml")
		res = soup.findAll("article", {"class": "listingItem"})
		for r in res:
		     print("Company Name: " + r.find('a').text)
		     print("Address: " + r.find("div", {'class': 'address'}).text)
		     print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)
		print "Data retrieved and stored in document"
		count += 1
	else:
		break
		driver.quit()
driver.quit()		
