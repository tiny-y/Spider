# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_kanxue(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '/html/body/main/div/div[2]/div[2]/table/tbody'
               #/html/body/main/div/div[2]/div[2]/table/tbody/tr[1]/td/div[1]/a[2]

    def title_xpath(self):
        return '/td/div[1]/a[2]'

    def url_xpath(self):
        return '/td/div[1]/a[2]/@href'

    def date_xpath(self):
        return '/td/div[2]/div[1]/span[1]'

    def category_xpath(self):
        return '/td/div[1]/a[3]'

    def load_more_xpath(self):
        return '/html/body/main/div/nav/ul/li[last()]/a'

    def count_divs_class(self):
        return 'thread'

    def web_site(self):
        return 'https://bbs.kanxue.com/new-tid.htm'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/tr[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/tr[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/tr[{idx}]{self.date_xpath()}"
        category_xpath = f"{self.root_xpath()}/tr[{idx}]{self.category_xpath()}"
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '看雪'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//tr[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return "/html/body/header/div/nav/div[1]/ul/li[9]/form/div/input"
