# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 19:50 
# @Author  : gzy
from xpath import XpathRules


class XPathRules_fanka(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '/html/body/div/div[4]/div/div[1]/ul'

    def title_xpath(self):
        return '/div/a'

    def url_xpath(self):
        return '/div/a/@href'

    def date_xpath(self):
        return '/div/div/div/span/text()'

    def category_xpath(self):
        return '/html/body/div/div[4]/div/div[1]/ul/li[1]/div/div/a'

    def load_more_xpath(self):
        return '/html/body/div/div[4]/div/div[1]/div[2]/a[7]'

    def count_divs_class(self):
        return 'list_text'

    def web_site(self):
        return 'https://www.kafan.cn/tech/'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/li[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/li[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/li[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '饭卡网'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
