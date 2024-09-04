# -*- coding: utf-8 -*-
# @Time    : 2024/08/21 14:40 
# @Author  : gzy

# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:48
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from spider.xpath import XpathRules


class XPathRules_labs(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div/div/div/div[2]'

    def title_xpath(self):
        return '/a/div/div/h5/font/font'

    def url_xpath(self):
        return '/a/@href'

    def date_xpath(self):
        return '/a/div/div/div[1]/small/font/font'

    def category_xpath(self):
        return '/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div/div/div/div[1]/div[2]/label/select/option[1]/font/font'

    def load_more_xpath(self, cur=None):
        return '/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[6]/div/div/div/div/div/div[3]/a[2]'

    def count_divs_class(self):
        return 'page-filter__item'

    def web_site(self):
        return 'https://labs.withsecure.com/publications'

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
        return "Medium"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//div[@class="{class_name}"]'
        return xpath_expr
