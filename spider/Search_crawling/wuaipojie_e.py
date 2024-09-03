# -*- coding: utf-8 -*-
# @Time    : 2024/08/15 17:04
# @Author  : gzy
from xpath import XpathRules


class XPathRules_52pojie(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[6]/div[2]/div/div/div[3]/div[2]/table'


    def title_xpath(self):
        return '/tr/th/a[1]'

    def url_xpath(self):
        return '/tr/th/a[1]/@href'

    def date_xpath(self):
        return '/tr/td[3]/em/span/text()'

    def category_xpath(self):
        return '/html/body/div[6]/div[2]/div/div/div[3]/div[2]/table/tbody[1]/tr/td[2]/a'

    def load_more_xpath(self):
        return '/html/body/div[6]/div[2]/div/div/div[4]/div/a[8]'

    def count_divs_class(self):
        return 'common'

    def web_site(self):
        return 'https://www.52pojie.cn/forum.php?mod=guide&view=tech&page=1'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/tbody[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/tbody[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/tbody[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return '吾爱破解'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//th[@class="{class_name}"]'
        return xpath_expr



