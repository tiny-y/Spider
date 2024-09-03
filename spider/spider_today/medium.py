
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_medium(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[1]/div[2]/div/div[4]/div[2]/section/div[1]'

    def title_xpath(self):
        return '/div[2]/a/h3/div/font/font'

    def url_xpath(self):
        return '/div[2]/a/@href'

    def date_xpath(self):
        return '/div[2]/div/div/div[2]/div/time/font/font'

    def category_xpath(self):
        return '/html/body/div[1]/div[2]/div/div[3]/div/div[1]/header/div/div/div[2]/a/h1/font/font'

    def load_more_xpath(self):
        return ''

    def count_divs_class(self):
        return 'u-lineHeightBase postItem'

    def web_site(self):
        return 'https://medium.com/mitre-attack'

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
        return "W/Lbs"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
