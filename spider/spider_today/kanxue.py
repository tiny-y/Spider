# -*- coding: utf-8 -*-
# @Time    : 2024/08/21 09:59 
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:48
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_kanxue(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/main/div/div/div[2]/table/tbody'

    def title_xpath(self):
        return '/td/div[1]/a[2]'

    def url_xpath(self):
        return '/td/div[1]/a[2]/@href'

    def date_xpath(self):
        return '/td/div[2]/div[1]/span1'

    def category_xpath(self):
        return '/td/div[1]/a[3]'

    def load_more_xpath(self, cur=None):
        return '/html/body/main/div/nav/ul/li[12]/a'

    def count_divs_class(self):
        return 'thread'

    def web_site(self):
        return 'https://bbs.kanxue.com/new-digest.htm'

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
