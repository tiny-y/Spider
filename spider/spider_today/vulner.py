# -*- coding: utf-8 -*-
# @Time    : 2024/08/21 15:49 
# @Author  : gzy
# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 20:06
# @Author  : gzy
from xpath import XpathRules


class XPathRules_vulner(XpathRules):
    """特定网站的 XPath 规则"""

    def root_xpath(self):
        return '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]'

    def title_xpath(self):
        return '/div[1]/div[2]/p[1]/font/font'

    def url_xpath(self):
        return '/a[2]/@href'

    def date_xpath(self):
        return '/div[1]/div[1]/span[3]/font/font'

    def category_xpath(self):
        return '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div/a[1]/div/span[1]/span/font/font'

    def load_more_xpath(self):
        return '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div[2]/nav/ul/li[9]'

    def count_divs_class(self):
        return 'css-9oa0ui-SearchResultItem-container'

    def web_site(self):
        return 'https://vulners.com/search?query=viewCount:[50%20TO%20*]%20order:viewCount%20last%207%20days'

    def extract_element(self, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        title_xpath = f"{self.root_xpath()}/a[{idx}]{self.title_xpath()}"
        url_xpath = f"{self.root_xpath()}/a[{idx}]{self.url_xpath()}"
        date_xpath = f"{self.root_xpath()}/a[{idx}]{self.date_xpath()}"
        category_xpath = self.category_xpath()
        return title_xpath, url_xpath, date_xpath, category_xpath

    def web_name(self):
        return "Vulner"

    def count_divs_xpath(self):
        class_name = self.count_divs_class()
        xpath_expr = f'{self.root_xpath()}//a[@class="{class_name}"]'
        return xpath_expr
