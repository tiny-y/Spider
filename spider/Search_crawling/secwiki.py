# -*- coding: utf-8 -*-
# @Time    : 2024/08/16 11:25 
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/16 09:58
# @Author  : gzy
from spider.xpath import XpathRules


class XpathRules_seck(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = search_term

    def root_xpath(self):
        return '/html/body/div[2]/div/div/div/div/div/table/tbody'

    def title_xpath(self):
        return '/td[2]/a'

    def url_xpath(self):
        return '/td[2]/a/@href'

    def date_xpath(self):
        return '/td[1]'

    def category_xpath(self):
        return '/td[3]/a'

    def load_more_xpath(self, cur=None):
        return '//*[@id="yw1"]/li[13]/a'

    def count_divs_class(self):
        return 'button-column'

    def web_site(self):
        return 'https://www.sec-wiki.com/news/search'

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
        return 'sec-wiki'

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//td[@class="{class_name}"]'
        return xpath_expr

    def search_box_xpath(self):
        return '//*[@id="yii_bootstrap_collapse_0"]/form/input'
