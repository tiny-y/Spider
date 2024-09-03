# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:48 
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_zhidao(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term
        self.first_call = True

    def root_xpath(self):
        return '/html/body/div[2]/div/div/div[2]/table/tbody'

    def title_xpath(self):
        return '/td[4]/a'

    def url_xpath(self):
        return '/td[4]/a/@href'

    def date_xpath(self):
        return '/td[2]'

    def category_xpath(self):
        return '/html/body/div[2]/div/div/form/div/h2'

    def load_more_xpath(self):
        if self.first_call:
            # 如果是第一次调用，返回第一个 XPath
            self.first_call = False  # 设置为 False，表示已经调用过了
            return '/html/body/div[2]/div/div/nav/ul/li[6]/a/span/i'
        else:
            # 之后的调用返回另一个 XPath
            return '/html/body/div[2]/div/div/nav/ul/li[7]/a/span/i'

    def count_divs_class(self):
        return 'vul-title-wrapper'

    def web_site(self):
        return 'https://www.seebug.org/search/'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/tr[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/tr[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/tr[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '知道创宇'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//td[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '//*[@id="sea-condition"]'
