from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("drivers/chromedriver.exe")
driver.get("https://eksisozluk.com/")

def getEntries(searchedItem):
    pageCounter = 1
    entryCounter = 1

    searchBox = driver.find_element_by_id("search-textbox")
    searchBox.send_keys(searchedItem)
    searchBox.send_keys(Keys.ENTER)

    title = driver.find_element_by_id("title").text

    try:
        if(driver.find_element_by_xpath("//*[@id='topic']/div[4]/a[1]").is_displayed()):
            pageNumber = driver.find_element_by_xpath("//*[@id='topic']/div[4]/a[1]").text
    except:
        pageNumber = 1

    url = driver.current_url
    for i in range(int(pageNumber)):
        driver.get(str((url+"?p="+str(pageCounter))))
        entries = driver.find_elements_by_class_name("content")
        for entry in entries:
            print(f"entry {entryCounter} for {title} \n")
            print(entry.text+"\n")
            print("-----------------------------------------------------\n")
            entryCounter+=1
        pageCounter+=1
    driver.close()

getEntries("python")

