from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://vnexpress.net/gdp-nam-2020-co-the-chi-tang-5-96-4054079.html"

browser = webdriver.Chrome()
browser.get(url)

title = browser.find_element_by_class_name('title-detail')
description = browser.find_element_by_class_name('description')
texts = browser.find_elements_by_class_name('Normal')

len_text = len(texts)

print(title.text)
print(description.text)

for i in range(len_text):
    print(texts[i].text)

browser.quit()