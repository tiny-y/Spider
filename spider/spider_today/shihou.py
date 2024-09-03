# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06 
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_sihou(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[4]/div[2]/section/article[1]/div/div[2]/div'

    def title_xpath(self):
        return '/li/div/a/h1'

    def url_xpath(self):
        return '/li/div/a/@href'

    def date_xpath(self):
        return '/li/div/div/p/text()'

    def category_xpath(self):
        return '/html/body/div[4]/div[2]/section/article[1]/div/div[1]/text()[2]'

    def load_more_xpath(self):
        return '/html/body/div[4]/div[2]/section/article[1]/div/div[3]/a'

    def count_divs_class(self):
        return 'new_con'

    def web_site(self):
        return 'https://www.4hou.com/category/news'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/div[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/div[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/div[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '嘶吼'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
