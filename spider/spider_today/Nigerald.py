
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:48
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_nigerald(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[2]/div/div/div'

    def title_xpath(self):
        return '/a/h2/font/font'

    def url_xpath(self):
        return '/div[3]/a/@href'

    def date_xpath(self):
        return '/p/font/font'

    def category_xpath(self):
        return '/div[4]/a[1]'

    def load_more_xpath(self):
        return '/html/body/div[2]/div/div/ul/li/a'

    def count_divs_class(self):
        return 'post-entry'

    def web_site(self):
        return 'https://dtsec.us/'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/article[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/article[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/article[{idx}]{self.date_xpath()}"
        category_xpath = f"{self.root_xpath()}/article[{idx}]{self.category_xpath()}"
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return "Nigerald's Blog"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
