from modules.crawler import SuperWebCrawler
from config import ConfigURL

configURL = ConfigURL.generate_config_object()
crawler = SuperWebCrawler(configURL)

url = "https://cafef.vn/imf-du-bao-viet-nam-tang-truong-gdp-65-trong-nam-2019-20190717102838593.chn"
crawler.run_program(url, "1234")