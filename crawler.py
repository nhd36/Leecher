from selenium import webdriver
from config import configURL

class SuperWebCrawler:
    def __init__(self, url):
        self.url = url
        self.web_driver = None

    def init_selenium(self):
        print("Brower options for using SuperDuperWebCrawler: firefox/edge/chrome/safari/opera")
        browser_options = input("Enter your chosen browser: ")
        if browser_options.lower() == "firefox":
            driver = webdriver.Firefox()
        elif browser_options.lower() == "edge":
            driver = webdriver.Edge()
        elif browser_options.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser_options.lower() == "safari":
            driver = webdriver.Safari()
        elif browser_options.lower() == "opera":
            driver = webdriver.Opera()
        else:
            print("Browser not found.")
            return None

        return driver

    def filter_div(self):
        for domain in configURL.keys():
            if self.url.startswith(domain):
                title_filter = self.get_filter_selector(configURL[domain]["title"])
                description_filter = self.get_filter_selector(configURL[domain]["description"])
                content_filter = self.get_filter_selector(configURL[domain]["content"])
                return title_filter, description_filter, content_filter
        return None

    def get_filter_selector(self, component):
        tag = component["tag"]
        filter_str = f"//{tag}"
        tag_selectors = component["tag_selector"]
        for tag_selector in tag_selectors.keys():
            selector_attribute = tag_selectors[tag_selector]
            filter_selector = f"[@{tag_selector}='{selector_attribute}']"
            filter_str += filter_selector
        return filter_str

    def run_program(self):
        self.web_driver = self.init_selenium()
        if not self.web_driver:
            return None
        self.web_driver.set_page_load_timeout(30)
        self.web_driver.get(self.url)
        if not self.filter_div():
            return None
        title_filter, description_filter, content_filter = self.filter_div()
        title = self.web_driver.find_elements_by_xpath(title_filter)
        title_str = ""
        for element in title:
            title_str += element.text.replace("\n", "") + " "
        description = self.web_driver.find_elements_by_xpath(description_filter)
        description_str = ""
        for element in description:
            description_str += element.text.replace("\n", "") + " "
        content = self.web_driver.find_elements_by_xpath(content_filter)
        content_str = ""
        for element in content:
            content_str += element.text.replace("\n", "") + " "

        json_return = {
            "title": title_str,
            "description": description_str,
            "content": content_str
        }
        self.web_driver.quit()
        return json_return

url_1 = "https://dantri.com.vn/kinh-doanh/cpi-quy-12009-tang-1447-1238078209.htm"
url_2 = "https://dantri.com.vn/kinh-doanh/10-thang-cpi-di-chua-duoc-13-muc-tieu-ca-nam-1414756047.htm"
supercrawler = SuperWebCrawler(url_1)
print(supercrawler.run_program())