# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06 
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_sihou(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '//*[@id="container"]'

    def title_xpath(self):
        return '/div/a/h1'

    def url_xpath(self):
        return '/div/a/@href'

    def date_xpath(self):
        return '/div/div/div[1]/span'

    def category_xpath(self):
        return '/a/div/span'

    def load_more_xpath(self, cur=None):
        return '//*[@id="container"]/div/a[3]'

    def count_divs_class(self):
        return 'new_con'

    def web_site(self):
        return 'https://www.4hou.com/search-post'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/li[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/li[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/li[{idx}]{self.date_xpath()}"
        category_xpath = f"{self.root_xpath()}/li[{idx}]{self.category_xpath()}"
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '嘶吼'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '//*[@id="container"]/div/div/div/div[1]/form/input'
