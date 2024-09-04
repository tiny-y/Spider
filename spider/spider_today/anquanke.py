# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 19:37 
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_anquanke(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/main/div/div/div[1]/div/div[2]'

    def title_xpath(self):
        return '/div/div[2]/div/div[1]/a'

    def url_xpath(self):
        return '/div/div[2]/div/div[1]//@href'

    def date_xpath(self):
        return '/div/div[2]/div/div[4]/div[1]/span/span/text()'

    def category_xpath(self):
        return '/html/body/main/div/div/div[1]/div/div[1]/h1'

    def web_name_xpath(self):
        return '/html/body/main/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[4]/div[1]/a/span'

    def load_more_xpath(self, cur=None):
        return '/html/body/main/div/div/div[1]/div/div[3]/button'

    def count_divs_class(self):
        return 'info-content'

    def web_site(self):
        return 'https://www.anquanke.com/news'

    def extract_element(self, idx):
        title_xpath = f"{self.root_xpath()}/div[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/div[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/div[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '安全客'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr



