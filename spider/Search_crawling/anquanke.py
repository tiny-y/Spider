# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 19:37 
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_anquanke(XpathRules):

    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '/html/body/main/div[2]/div/div/div[1]/div/div[3]'

    def title_xpath(self):
        return '/div/a/div'

    def url_xpath(self):
        return '/div/a/@href'

    def date_xpath(self):
        return '/div/div[1]/span'

    def category_xpath(self):
        return '/html/body/main/div[1]/div/div/div[2]/div/div/ul/li[1]/a'

    def load_more_xpath(self, cur=None):
        return '/html/body/main/div[2]/div/div/div[1]/div/div[4]/div'

    def count_divs_class(self):
        return 'search-result-item'

    def web_site(self):
        return 'https://www.anquanke.com/news'

    def extract_element(self, idx):
        title_xpath = f"{self.root_xpath()}/div[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/div[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/div[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '安全客'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '/html/body/header/div/div/div[1]/div[1]/fieldset/div/input'


