# -*- coding: utf-8 -*-


from spider.xpath import XpathRules


class XPathRules_t001s(XpathRules):
    """特定网站的 XPath 规则"""

    def __init__(self, search_term):
        self.search_term = f"site:t00ls.net {search_term}"

    def root_xpath(self):
        # 返回 roots 列表中的每一个 root
        roots = [
            '//*[@id="rso"]/div[1]/div',
            '//*[@id="rso"]/div[2]',
            '//*[@id="rso"]/div[1]',
            '//*[@id="rso"]',
        ]
        return roots

    def title_xpath(self):
        titles = [
            '/div/div/div[1]/div/div/span/a/h3',
            '/div/div/div[2]/g-section-with-header/div[1]/a/span',
            '/div/div/div/div[1]/div/div/span/a/h3'
        ]

        return titles


    def url_xpath(self):
        return '/div/div/div[1]/div/div/span/a/@href'

    def date_xpath(self):
        return '/div/div/div[2]/div/span[1]/span'

    def category_xpath(self):
        return ("/html/body/div[3]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div["
                "1]/div/div/span/a/div/div/div/div[1]/span")

    def load_more_xpath(self):
        return '/html/body/div[3]/div/div[12]/div/div[4]/div/div[3]/table/tbody/tr/td[10]/a/span[2]'

    def count_divs_class(self):
        return 'MjjYud'

    def web_site(self):
        return 'https://www.google.com/'

    def extract_element(self, tree, idx):
        """
        获取爬取的元素
        :param idx:
        :return:
        """
        # 尝试 roots 列表中的每一个 root
        for root in self.root_xpath():
            for title in self.title_xpath():
                title_xpaths = [
                    f"{root}/div[{idx}]{title}",
                    f"{root}{title}",
                ]
                for t in title_xpaths:
                    title_xpath = t
                    url_xpath = f"{root}/div[{idx}]{self.url_xpath()}"
                    date_xpath = f"{root}/div[{idx}]{self.date_xpath()}"
                    category_xpath = self.category_xpath()
                    if tree.xpath(title_xpath) and tree.xpath(date_xpath):  # 检查 title_xpath 是否存在
                        # 如果存在，返回路径
                        return title_xpath, url_xpath, date_xpath, category_xpath

        # 如果没有找到任何匹配项，抛出异常
        raise XPathNotFoundException(f"无法找到对应的路径.")

    def web_name(self):
        return 't00ls'

    def count_divs_xpath(self, tree):
        class_name = self.count_divs_class()
        for root in self.root_xpath():
            xpath_expr = f'{root}//div[@class="{class_name}"]'
            if len(tree.xpath(xpath_expr)) > 5:
                return xpath_expr
        raise XPathNotFoundException(f"无法找到对应的元素路径.")

    def search_box_xpath(self):
        return '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'


class XPathNotFoundException(Exception):
    """自定义异常：当找不到匹配的 XPath 时抛出"""
    pass
