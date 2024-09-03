# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 17:04 
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_freebuf(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[1]/div/div/section/main/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]'

    def title_xpath(self):
        return '/div[1]/div/a[1]/span'

    def url_xpath(self):
        return '/div[1]/div/a[1]/@href'

    def date_xpath(self):
        return '/div[2]/div/div/p[2]/span'

    def category_xpath(self):
        return '/html/body/div[1]/div/div/section/main/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/a/p/span'

    def load_more_xpath(self):
        return '/html/body/div[1]/div/div/section/main/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/p/span'

    def web_site(self):
        return 'https://www.freebuf.com'

    def count_divs_class(self):
        return 'title-view'

    def extract_element(self, idx):
        title_xpath = f"{self.root_xpath()}/div[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/div[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/div[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return 'freebuf'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
