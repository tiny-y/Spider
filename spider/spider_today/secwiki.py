# -*- coding: utf-8 -*-
# @Time    : 2024/08/16 11:25 
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/16 09:58
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_seck(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]'

    def title_xpath(self):
        return '/a[1]'

    def url_xpath(self):
        return '/a[1]/@href'

    def date_xpath(self):
        return '/span'

    def category_xpath(self):
        return '/html/body/div[2]/div/div/div/div[1]/div[2]/div/ul/li[1]'

    def load_more_xpath(self, cur=None):
        return ' '

    def count_divs_class(self):
        return 'dropcap'

    def web_site(self):
        return 'https://www.sec-wiki.com/index.php'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/p[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/p[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/p[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return 'sec-wiki'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//span[@class="{class_name}"]'
        return xpath_expr

