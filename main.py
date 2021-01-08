from modules.crawler import SuperWebCrawler
from config import ConfigURL

configURL = ConfigURL.generate_config_object()
crawler = SuperWebCrawler(configURL)

url = "http://tapchitaichinh.vn/tai-chinh-quoc-te/kinh-te-trung-quoc-tang-truong-vuot-muc-du-bao-trong-quy-ii-325636.html"
crawler.run_program(url, "1234")