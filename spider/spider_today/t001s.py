# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 09:24 
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_t001s(XpathRules):
    """特定网站的 XPath 规则"""
    def __init__(self):
        super().__init__()

    def root_xpath(self):
        return '/html/body/div/section/div/div/div[1]/div[2]'

    def title_xpath(self):
        return '/div/div/div[2]/h4/a'

    def url_xpath(self):
        return '/div/div/div[2]/h4/a/@href'

    def date_xpath(self):
        return '/div/div/div[2]/div/span[1]/span/@title'

    def category_xpath(self):
        return '/html/body/div/section/div/div/div[1]/div[1]/h1'

    def load_more_xpath(self,cur=None):
        return '/html/body/div/section/div/div/div[1]/div[3]/a/span'

    def count_divs_class(self):
        return 'item_content'

    def web_site(self):
        return 'https://www.t00ls.com/news.html'

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
        return 't00ls'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr

