# -*- coding: utf-8 -*-
# @Time    : 2024/08/20 18:22 
# @Author  : gzy
from abc import ABC, abstractmethod


class XpathRules(ABC):
    """抽象的 XPath 规则基类"""

    def __init__(self):
        self.search_term = None

    @abstractmethod
    def root_xpath(self):
        pass

    @abstractmethod
    def title_xpath(self):
        pass

    @abstractmethod
    def url_xpath(self):
        pass

    @abstractmethod
    def date_xpath(self):
        pass

    @abstractmethod
    def category_xpath(self):
        pass

    @abstractmethod
    def load_more_xpath(self, cur=None):
        pass

    def count_divs(self):
        pass

    def web_site(self):
        pass

    def extract_element(self, idx):
        pass

    def web_name(self):
        pass

    def count_divs_xpath(self):
        pass

    def search_box_xpath(self):
        pass
