# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_mcafee(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[2]/article/div/div/div[2]/div[2]'

    def title_xpath(self):
        return '/div[2]/h5/a/font/font'

    def url_xpath(self):
        return '/div[2]/h5/a/@href'

    def date_xpath(self):
        return '/div[3]/p/small[1]/font/font'

    def category_xpath(self):
        return '/html/body/div[2]/div/p/span/span[3]/font/font'

    def load_more_xpath(self):
        return '/html/body/div[2]/article/div/div/div[2]/div[3]/div/div/ul/li[5]/a'

    def count_divs_class(self):
        return 'card-body'

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
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return "McAfee"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
