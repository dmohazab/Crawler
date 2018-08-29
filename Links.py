#Written by Danial Mohazab
#Python Script to Grab WebPage Links

from bs4 import BeautifulSoup
from xlwt import Workbook
import urllib.request
import ssl

wb = Workbook()

url = "https://htcwdpstgweb.azurewebsites.net/fr-ca/privacy/"     #Modify this for links

newName = "Privacy"                                            #Modify this

ssl._create_default_https_context = ssl._create_unverified_context

sheet1 = wb.add_sheet(newName)
resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
sheet1.write(0,0,"Title")
sheet1.write(0,1,"Links")
sheet1.col(0).width = 7500
sheet1.col(1).width = 15000

for i,link in enumerate(soup.find_all('a', href=True)):
    if link['href'] == "#":
        sheet1.write(i+1, 1, "Dropdown Menu")
    elif "javascript" in link['href']:
        continue
    elif ".aspx" in link['href']:
        if ("https://htcwdpstgweb.azurewebsites.net/fr-ca/" + str(link['href'])).count("http")>1:
            sheet1.write(i + 1, 1, str(link['href']))
        else:
            sheet1.write(i+1, 1, "https://htcwdpstgweb.azurewebsites.net/fr-ca/" + str(link['href']))
    elif "carousel" in link['href']:
        continue
    elif "homecapital" in url:
        if ".pdf" in link['href'] or ".asp" in link['href']:
            sheet1.write(i + 1, 1, "http://www.homecapital.com/" + str(link['href']))
    elif "http" not in link['href']:
        if "homecapital" in link['href']:
            pass
        else:
            sheet1.write(i + 1, 1, "https://htcwdpstgweb.azurewebsites.net" + str(link['href']))
    else:
        sheet1.write(i+1,1,link['href'])
    sheet1.write(i+1,0,str(link.string).replace(':', ''))

wb.save('WebApp\\' + newName + '.xls')

