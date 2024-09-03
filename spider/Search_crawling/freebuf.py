# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 17:04 
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_freebuf(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '/html/body/div[1]/div/div/section/main/div/div/div[2]/div/div[2]/div/div[2]'

    def title_xpath(self):
        return '/div/a[1]/div'

    def url_xpath(self):
        return '/div/a[1]/@href'

    def date_xpath(self):
        return '/a/div/div[2]/div[2]/div[2]/div[2]'

    def category_xpath(self):
        return '/html/body/div[1]/div/div/section/main/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]'

    def load_more_xpath(self):
        return None

    def web_site(self):
        return 'https://www.freebuf.com/search?activeType=1'

    def count_divs_class(self):
        return 'result-item'

    def extract_element(self, idx):
        title_xpath = f"{self.root_xpath()}/div[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/div[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/div[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return 'freebuf'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '/html/body/div[1]/div/div/section/main/div/div/div[1]/div/span/input'


