# -*- coding: utf-8 -*-
# @Time    : 2024/08/16 09:58 
# @Author  : gzy

from spider.xpath import XpathRules


class XpathRules_blog(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '/html/body/div/div[1]/div/div[1]/div[1]'

    def title_xpath(self):
        return '/div/h2/a'

    def url_xpath(self):
        return '/div/h2//@href'

    def date_xpath(self):
        return '/footer/div/ul/li[3]/text()'

    def category_xpath(self):
        return '/html/body/div/div[1]/div/div[1]/div[1]/article[1]/footer/div/ul/li[5]/a'

    def web_name_xpath(self):
        return '/html/body/div/header/div[1]/div/div[1]//@title'

    def load_more_xpath(self):
        return ' '

    def count_divs_class(self):
        return 'post-entry-details full-width'

    def web_site(self):
        return 'https://blog.topsec.com.cn'

    def extract_element(self, idx):
        """
        获取元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/article[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/article[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/article[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '阿尔法实验室'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return "/html/body/div/header/div[2]/div[1]/div[1]/form/input"
