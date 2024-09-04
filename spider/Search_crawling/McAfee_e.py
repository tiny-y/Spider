# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_mcafee(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term
        self.first_call = True

    def root_xpath(self):
        return '//*[@id="short-header"]/div[2]/article/div/div/div[1]/div[2]'

    def title_xpath(self):
        return '/div[2]/h5/a'

    def url_xpath(self):
        return '/div[2]/h5/a/@href'

    def date_xpath(self):
        return '/div[3]/p/small[1]'

    def category_xpath(self):
        return '/div[2]/span[1]/font/font'

    def load_more_xpath(self, cur=None):
        if self.first_call:
            # 如果是第一次调用，返回第一个 XPath
            self.first_call = False  # 设置为 False，表示已经调用过了
            return '//*[@id="short-header"]/div[2]/article/div/div/div[1]/div[3]/div/div/ul/li[5]/a'
        else:
            # 之后的调用返回另一个 XPath
            return '//*[@id="short-header"]/div[2]/article/div/div/div[1]/div[3]/div/div/ul/li[7]/a'

    def count_divs_class(self):
        return 'card'

    def web_site(self):
        return 'https://www.mcafee.com/blogs/other-blogs/mcafee-labs/'

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
        return "McAfee"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '//*[@id="navbar3"]/form[1]/div[2]/input'
