from selenium import webdriver
import json

class SuperWebCrawler:
    def __init__(self, configURL):
        self.configURL = configURL

    def init_selenium(self):
        try:
            options = webdriver.FirefoxOptions()
            options.headless = True
            driver = webdriver.Firefox(options=options)
        except Exception as ex:
            print(ex)
            return None
        return driver

    def filter_div(self, url):
        for domain in self.configURL.keys():
            if domain in url:
                title_filter = self.get_filter_selector(self.configURL[domain]["title"])
                description_filter = self.get_filter_selector(self.configURL[domain]["description"])
                content_filter = self.get_filter_selector(self.configURL[domain]["text"])
                return title_filter, description_filter, content_filter, domain
        return None

    def output_json(self, dict_data, link_index):
        with open(f"result/json/{link_index}.json", "w+") as write_file:
            json.dump(dict_data, write_file)

    def output_txt(self, title, description, content, link_index):
        write_str = f"{title}\n{description}\n{content}"
        with open(f"result/txt/{link_index}.txt", "w+") as write_file:
            write_file.write(write_str)

    def get_filter_selector(self, component):
        tag = component["tag"]
        filter_str = f"//{tag}"
        tag_selectors = component["tag_selector"]
        for tag_selector in tag_selectors.keys():
            selector_attribute = tag_selectors[tag_selector]
            filter_selector = f"[@{tag_selector}='{selector_attribute}']"
            filter_str += filter_selector
        return filter_str

    def crawl_web(self, url):
        self.web_driver = self.init_selenium()
        if not self.web_driver:
            return None
        self.web_driver.set_page_load_timeout(30)
        self.web_driver.get(url)
        if not self.filter_div(url):
            return None
        title_filter, description_filter, content_filter, domain = self.filter_div(url)
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

        self.web_driver.quit()
        return {
            "domain": domain,
            "status": "success",
            "result":{
                "title": title_str,
                "description": description_str,
                "content": content_str
            }
        }

    def run_program(self, url, link_index):
        json_data = self.crawl_web(url)
        if not json_data:
            print("Error. Cannot crawl web")
            return
        txt_data = json_data["result"]
        self.output_json(json_data, link_index)
        self.output_txt(
            txt_data["title"],
            txt_data["description"],
            txt_data["content"],
            link_index)