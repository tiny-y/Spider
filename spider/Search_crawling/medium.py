
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_medium(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div[2]/div'

    def title_xpath(self):
        return '/article/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/a/h2'

    def url_xpath(self):
        return '/article/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/a/@href'

    def date_xpath(self):
        return '/article/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span/div/div[1]/span'

    def category_xpath(self):
        return '/article/div/div/div/div/div[1]/div/div[1]/div/div[4]/div/div/a/p/font/font'

    def load_more_xpath(self, cur):
        return f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div[2]/div/div[{cur}]/div/div/button'
               #//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div[2]/div/div[40]/div/div/button

    def count_divs_class(self):
        return 'bh cm'

    def web_site(self):
        return 'https://medium.com/mitre-attack/search'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/div[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/div[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/div[{idx}]{self.date_xpath()}"
        category_xpath = f"{self.root_xpath()}/div[{idx}]{self.category_xpath()}"
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return "W/Lbs"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '//*[@id="root"]/div/div[3]/div[1]/div[2]/div[1]/div/div/input'
