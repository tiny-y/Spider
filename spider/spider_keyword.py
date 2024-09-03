# -*- coding: utf-8 -*-
# @Time    : 2024/08/22 09:23
# @Author  : gzy
from models.models import db, Spider_info
from spider.model import *


class SpiderForKey(WebScraper):

    def __init__(self, xpath_rules: XpathRules):
        super().__init__(xpath_rules)
        self.search_box_xpath = self.obj.search_box_xpath()  # 搜索框的XPATH
        self.search_term = self.obj.search_term  # 搜索关键字

    def redirected_url(self):
        try:
            self.driver.get(self.web_site)  # 打开指定URL
            time.sleep(10)  # 等待页面加载
            search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)  # 定位搜索框
            search_box.clear()  # 清空搜索框
            search_box.send_keys(self.search_term)  # 输入搜索关键词
            search_box.send_keys(Keys.RETURN)  # 回车
            new_url = self.driver.current_url
            print(f"Redirected to: {new_url}")
            return new_url
        except Exception as e:
            print(e)

    def data_process(self, title_elements, url_elements, date_elements, category_elements, web_name,
                     filtered_elements, last_two_years, total, counts, today, date_format="%Y-%m-%d"):
        for date_text in date_elements:
            if isinstance(date_text, etree._Element):
                date_text = date_text.text
            if isinstance(date_text, str):
                date_text = self.extract_date(date_text)  # 返回了一个日期对象
                # 通过数量和近两年年份进行过滤
            if (total < 100 and counts < 100) or (date_text.year in last_two_years):
                title_text, category_text, url_text = self.element_text_processing(
                    title_elements, url_elements, category_elements)
                date_text = date_text.strftime(date_format)
                # 通过url判断爬取未爬取的元素
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
            else:
                return False

        return True

    def filter(self, tree, total, current_div_count, date_format="%Y-%m-%d"):
        """
        :param tree: tree对象
        :param date_format: 日期格式
        :return:
        """
        web_name = self.obj.web_name()
        current_year = datetime.now().year
        # 获取近两年的年份
        last_two_years = [current_year - 1, current_year]
        filtered_elements = []
        today = datetime.today().strftime(date_format)
        counts = current_div_count
        total = total
        for i in range(1, counts + 1):
            title_elements, url_elements, date_elements, category_elements = self.content_extractor.extract_elements(
                tree, i)
            if not self.data_process(title_elements, url_elements, date_elements, category_elements, web_name,
                                     filtered_elements, last_two_years, counts, total, today, date_format):
                return False, self.item_id
        return filtered_elements, self.item_id

    def main(self):
        """
        最终运行函数
        :return:
        """
        print("Scrape method called")
        self.driver.get(self.redirected_url())
        time.sleep(3)
        tree = self.content_extractor.parse_content(self.driver.page_source)
        pre = 0
        total = 0
        spider_data = []
        while True:
            current_div_count = self.content_extractor.count_divs_num(tree)
            print(current_div_count)
            filtered_elements, self.item_id = self.filter(tree, total, current_div_count)
            for i in filtered_elements:
                print(i)
            if not filtered_elements:
                break
            else:
                # 尝试点击“加载更多”
                if self.click_load_more(current_div_count):
                    total = len(self.item_id)
                else:
                    # 滚动加载检查
                    if len(filtered_elements) == current_div_count - pre:
                        self.go_on_scroll()  # 如果上次和本次的元素数相等，进行滚动
                        pre = current_div_count
                    else:
                        break  # 如果不相等，跳出循环
                spider_data.extend(filtered_elements)
                # 等待页面加载并更新解析的HTML
                time.sleep(5)  # 等待加载
                updated_page_source = self.driver.page_source  # 获取更新后的页面源代码
                tree = self.content_extractor.parse_content(updated_page_source)  # 解析新的 HTML
            # 退出驱动程序
        self.driver_manager.quit_driver()
        return spider_data


from spider.Search_crawling.freebuf import XpathRules_freebuf
from spider.Search_crawling.anquanke import XpathRules_anquanke
from spider.Search_crawling.blog import XpathRules_blog
from spider.Search_crawling.kanxue import XpathRules_kanxue
from spider.Search_crawling.secwiki import XpathRules_seck
from spider.Search_crawling.McAfee_e import XpathRules_mcafee
from spider.Search_crawling.medium import XpathRules_medium
from spider.Search_crawling.zhidaochuanyu import XpathRules_zhidao
from spider.Search_crawling.shihou import XpathRules_sihou

if __name__ == '__main__':

    a = SpiderForKey(XpathRules_medium("car"))
    a.main()
