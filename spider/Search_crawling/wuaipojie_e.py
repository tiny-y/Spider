# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 17:04
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_52pojie(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = f"site:52pojie.cn {search_term}"

    def root_xpath(self):
        return '//*[@id="b_results"]'

    def title_xpath(self):
        return '/h2/a'

    def url_xpath(self):
        return '/div[1]/a/div[2]/div[2]/div/cite'

    def date_xpath(self):
        return '/div[2]/p/span'

    def category_xpath(self):
        return ''

    def load_more_xpath(self):
        return '//*[@id="b_results"]/li[12]/nav/ul/li[5]/a'

    def count_divs_class(self):
        return 'b_algo'

    def web_site(self):
        return 'https://www.bing.com/'

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
        return '吾爱破解'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//li[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '//*[@id="sb_form_q"]'
