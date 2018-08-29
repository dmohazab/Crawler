from selenium import webdriver
import xlrd
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
#Written by Danial Mohazab
#Python Script to screenshot based on excel links

folderName = "Privacy"     #Modify this

loc = "WebApp\\" + folderName + ".xls"

driver = webdriver.Chrome()

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(1,sheet.nrows):
    try:
        if sheet.cell_value(i,1) == "":
            continue
        elif sheet.cell_value(i,1) == "Dropdown Menu":
            continue
        elif (sheet.cell_value(i,1))[0] == "#":
            continue
        elif "mailto" in sheet.cell_value(i,1):
            continue
        else:
            driver.get(sheet.cell_value(i,1))
            if '.pdf' in str(sheet.cell_value(i,1)):
                time.sleep(3)
            WebDriverWait(driver, 1)
            if sheet.cell_value(i, 0) == "None":
                driver.save_screenshot("Screenshots\\" + folderName + "\\" + str(i+1) + ".png")
            else:
                driver.save_screenshot("Screenshots\\" + folderName + "\\" + str(sheet.cell_value(i, 0)) + ".png")
    except:
        driver.get("https://i.ytimg.com/vi/p28pePKK7Pc/maxresdefault.jpg")
        WebDriverWait(driver, 5)
        driver.save_screenshot("Screenshots\\" + folderName + "\\" + "Error " + str(i+1) + str(sheet.cell_value(i, 0)) + ".png")

driver.quit()


