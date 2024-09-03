# -*- coding: utf-8 -*-
# @Time    : 2024/08/16 18:17
# @Author  : gzy
import re
from datetime import datetime, timedelta
from lxml import etree
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlsplit, urlunsplit, urljoin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from spider.spider_today.McAfee import XPathRules_mcafee
from spider.spider_today.Nigerald import XPathRules_nigerald
from spider.spider_today.anquanke import XPathRules_anquanke
from spider.spider_today.blog import XPathRules_blog
from spider.spider_today.fankawang import XPathRules_fanka
from spider.spider_today.freebuf import XPathRules_freebuf
from spider.spider_today.kanxue import XPathRules_kanxue
from spider.spider_today.labs import XPathRules_labs
from spider.spider_today.medium import XPathRules_medium
from spider.spider_today.secwiki import XPathRules_seck
from spider.spider_today.shihou import XPathRules_sihou
from spider.spider_today.t001s import XpathRules_t001s
from spider.spider_today.wuaipojie import XPathRules_52pojie
from spider.spider_today.zhidaochuanyu import XPathRules_zhidao
# from spider.spider_today.secwiki import XPathRules_seck
# from spider.spider_today.blog import XPathRules_blog
# from spider.spider_today.wuaipojie import XPathRules_52pojie
# from spider.spider_today.fankawang import XPathRules_fanka
# from spider.spider_today.shihou import XPathRules_sihou
# from spider.spider_today.zhidaochuanyu import XPathRules_zhidao
# from spider.spider_today.kanxue import XPathRules_kanxue
# from spider.spider_today.Nigerald import XPathRules_nigerald
# from spider.spider_today.labs import XPathRules_labs
# from spider.spider_today.medium import XPathRules_medium
# from spider.spider_today.McAfee import XPathRules_mcafee
from spider.xpath import XpathRules

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverManager:
    """
    负责管理 Selenium WebDriver 的初始化和设置
    """

    def __init__(self, wait_time=10):
        self.driver = self.init_driver(wait_time)

    def init_driver(self, wait_time):
        options = Options()
        # 隐藏 Selenium WebDriver 的痕迹
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument("--disable-blink-features=AutomationControlled")

        # 初始化 WebDriver
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(wait_time)

        # 移除 `navigator.webdriver` 属性
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # 通过 JavaScript 伪造一些常见属性，进一步隐藏自动化痕迹
        driver.execute_script("""
            Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
            Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
        """)

        return driver

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        return self.driver.quit()


class ContentExtractor:
    """负责页面内容的解析和提取"""

    def __init__(self, xpath_rules: XpathRules):
        self.xpath_rules = xpath_rules

    def parse_content(self, page_content):
        """
        得到DOM树
        :param page_content:
        :return: tree  element对象
        """
        soup = BeautifulSoup(page_content, 'lxml')
        tree = etree.HTML(str(soup))
        return tree

    def extract_data(self, tree, xpath_expr):
        """
        获取指定xpath的值
        :param tree:
        :param xpath_expr:
        :return:
        """
        try:
            divs = tree.xpath(xpath_expr)
            return divs
        except etree.XPathEvalError as e:
            return False

    def count_divs_num(self, tree):
        xpath_expr = self.xpath_rules.count_divs_xpath()
        divs = self.extract_data(tree, xpath_expr)
        return len(divs)

    def extract_elements(self, tree, idx):
        """
        获取爬取的元素
        """
        title_xpath, url_xpath, date_xpath, category_xpath = self.xpath_rules.extract_element(idx)
        title = self.extract_data(tree, title_xpath)
        url = self.extract_data(tree, url_xpath)
        date = self.extract_data(tree, date_xpath)  # 可用遍历
        category = self.extract_data(tree, category_xpath)
        return title, url, date, category


class WebScraper:
    """主爬虫类，负责控制爬取流程"""

    def __init__(self, obj: XpathRules):
        self.obj = obj
        self.web_site = str(self.obj.web_site())
        self.driver_manager = DriverManager(wait_time=10)
        self.driver = self.driver_manager.get_driver()
        self.driver.get(self.web_site)
        self.actions = ActionChains(self.driver)
        self.item_id = set()
        self.content_extractor = ContentExtractor(obj)

    def click_load_more(self):
        try:
            load_more_xpath = self.obj.load_more_xpath()
            load_more_button = self.driver.find_element(By.XPATH, load_more_xpath)
            # 使用 JavaScript 进行点击
            self.driver.execute_script("arguments[0].click();", load_more_button)
            time.sleep(3)
            return True
        except Exception as e:
            return False

    def go_on_scroll(self):
        """
        继续滚轮
        :return:
        """
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)  # 等待页面加载新的内容
            # self.scrape()
            return True
        except Exception:
            return False

    # 处理爬取的url
    def url_processing(self, url_text):
        self.item_id.add(url_text)  # 已爬取元素唯一标识
        parts = urlsplit(self.web_site)
        # 如果 url_text 是相对路径，使用 urljoin 转换为完整 URL
        if not urlsplit(url_text).scheme:  # 判断 url_text 是否包含 scheme (如 'http', 'https')
            new_path = parts.path.rsplit('/', 1)[0] + '/'
            base_url = urlunsplit((parts.scheme, parts.netloc, new_path, '', ''))
            url = urljoin(base_url, url_text)
        else:
            url = url_text
        return url

    # 处理爬取的title等
    def element_text_processing(self, title_elements, url_elements, category_elements):
        title_text = ''.join(title_elements[0].itertext()).strip() if title_elements else "title_text[0].text"
        category_text = (''.join(category_elements[0].itertext()).strip() if hasattr(category_elements[0], 'text')
                         else category_elements[0]) if category_elements else ""
        url_text = url_elements[0] if url_elements else ""
        return title_text, category_text, url_text

    def extract_date(self, date_text):
        # 去除字符串两端的空白字符和换行符
        if date_text.startswith(' ') or date_text.endswith(' ') or '\n' in date_text:
            date_text = date_text.strip()

        # 去除中间的多余空白字符
        if '  ' in date_text or '\t' in date_text:
            date_text = re.sub(r'\s+', '', date_text)

        # 处理 "几分钟前" 的情况
        minutes_ago_match = re.search(r"(\d+)分钟前", date_text)
        if minutes_ago_match:
            minutes_ago = int(minutes_ago_match.group(1))
            return datetime.now() - timedelta(minutes=minutes_ago)

        # 处理 "几小时前" 的情况
        hours_ago_match = re.search(r"(\d+)小时前", date_text)
        if hours_ago_match:
            hours_ago = int(hours_ago_match.group(1))
            return datetime.now() - timedelta(hours=hours_ago)

        # 处理 "几天前" 的情况
        days_ago_match = re.search(r"(\d+)天前", date_text)
        if days_ago_match:
            days_ago = int(days_ago_match.group(1))
            return datetime.now() - timedelta(days=days_ago)

        # 定义日期格式列表
        date_formats = [
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%Y年%m月%d日",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
        ]

        # 使用正则表达式匹配常见的日期格式
        regex_patterns = [
            r"(\d{4})-(\d{1,2})-(\d{1,2})",  # 2024-8-13
            r"(\d{4})/(\d{1,2})/(\d{1,2})",  # 2024/8/13
            r"(\d{4})年(\d{1,2})月(\d{1,2})日",  # 2024年8月13日
            r"(\d{4})-(\d{1,2})-(\d{1,2})\s(\d{1,2}):(\d{1,2}):(\d{1,2})",  # 2024-08-13 08:40:00
            r"(\d{4})-(\d{1,2})-(\d{1,2})\s(\d{1,2}):(\d{1,2})"  # 2024-8-1 14:41
        ]

        # 遍历正则表达式模式，尝试匹配
        for pattern, date_format in zip(regex_patterns, date_formats):
            match = re.search(pattern, date_text)
            if match:
                # 将提取的日期字符串与指定格式进行解析
                try:
                    return datetime.strptime(match.group(0), date_format)
                except ValueError:
                    continue  # 如果格式不匹配，继续下一个

        # 如果没有匹配到格式，返回 None
        return None

    def should_extract_date(self, date_text):
        return "发布于" in date_text or re.search(r"\d+小时前", date_text) is not None

    def process_elements(self, title_elements, url_elements, date_elements, category_elements, web_name,
                         filtered_elements, today, date_format='%Y-%m-%d'):
        """
        处理提取的元素，并将符合条件的内容加入到 filtered_elements 中
        """
        for date_text in date_elements:
            if isinstance(date_text, etree._Element):
                date_text = date_text.text
            # 检查并解析日期
            if self.should_extract_date(date_text):
                parsed_date = self.extract_date(date_text)
            else:
                try:
                    parsed_date = datetime.strptime(date_text.split(' ')[0], date_format)
                except ValueError:
                    continue  # 如果解析失败，跳过该元素
            if parsed_date and parsed_date.strftime(date_format) == today:
                title_text, category_text, url_text = self.element_text_processing(
                    title_elements, url_elements, category_elements)
                if url_text not in self.item_id:
                    url_text = self.url_processing(url_text)
                    filtered_elements.append({
                        'title': title_text,
                        'url': url_text,
                        'date': date_text,
                        'web_name': web_name,
                        'category': category_text,
                        'now_date': today
                    })

        return filtered_elements

    def filter_by_date(self, tree, date_format="%Y-%m-%d"):
        """
        根据当前日期过滤
        :param tree: tree对象
        :param date_format: 日期格式
        :return:
        """
        web_name = self.obj.web_name()
        today = datetime.today().strftime(date_format)
        filtered_elements = []
        counts = self.content_extractor.count_divs_num(tree)
        for i in range(1, counts + 1):
            title_elements, url_elements, date_elements, category_elements = self.content_extractor.extract_elements(
                tree, i)
            self.process_elements(title_elements, url_elements, date_elements, category_elements, web_name,
                                  filtered_elements, today, date_format)
        return filtered_elements, self.item_id

    def scrape(self):
        """
        最终运行函数
        :return:
        """
        spider_data = []
        pre = 0
        while True:
            tree = self.content_extractor.parse_content(self.driver.page_source)
            current_div_count = self.content_extractor.count_divs_num(tree)
            print(f"Current div count: {current_div_count}")
            filtered_elements, item_id = self.filter_by_date(tree)
            if not filtered_elements:
                break
            else:
                # 尝试点击“加载更多”
                if self.click_load_more():
                    total = len(self.item_id)
                else:
                    # 滚动加载检查
                    if len(filtered_elements) == current_div_count - pre:
                        self.go_on_scroll()  # 如果上次和本次的元素数相等，进行滚动
                        pre = current_div_count
                    else:
                        break  # 如果不相等，跳出循环
                spider_data.extend(filtered_elements)
        self.driver_manager.quit_driver()
        return spider_data


# 示例 URL 和数据库配置


if __name__ == '__main__':
    for specific_xpath_rules in [XPathRules_mcafee(), XPathRules_medium(), XPathRules_labs(), XPathRules_nigerald(),
                                 XPathRules_zhidao(), XPathRules_sihou(), XPathRules_fanka(), XPathRules_52pojie(),
                                 XPathRules_blog(), XPathRules_anquanke(), XpathRules_t001s(), XPathRules_seck(),
                                 XPathRules_freebuf(), XPathRules_kanxue()]:
        scraper = WebScraper(specific_xpath_rules)
        scraper.scrape()
# specific_xpath_rules = XPathRules_fanka()
# scraper = WebScraper(db_config, specific_xpath_rules)
# scraper.scrape()
