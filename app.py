from flask import Flask, jsonify
from models.models import db, Spider_info, Spider_today
from spider.spider_keyword import SpiderForKey
from spider.model import WebScraper
from spider.spider_keyword import *
from spider.model import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite3.db"  # 连接数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 初始化数据库
with app.app_context():
    db.create_all()


# 定义一个视图来调用爬虫并存储数据
@app.route('/<search>')
def scrape_data(search):
    # 初始化 XPath 规则类（这里是一个示例，你可以根据需要使用不同的规则类）
    for specific_xpath_rules in [XpathRules_freebuf(search), XpathRules_kanxue(search), XpathRules_anquanke(search),
                                 XpathRules_blog(search), XpathRules_seck(search),XpathRules_medium(search),
                                 XpathRules_sihou(search), XpathRules_zhidao(search)]:

        spider = SpiderForKey(specific_xpath_rules)

        # 调用爬虫的 main 方法并获取爬取结果
        scraped_items = spider.main()
        # 保存数据到 SQLite 数据库
        for item in scraped_items:
            new_record = Spider_info(
                title=item.get('title'),
                url=item.get('url'),
                date=item.get('date'),
                web_name=item.get('web_name'),
                category=item.get('category'),
                now_date=item.get('now_date')
            )
            db.session.add(new_record)

        try:
            db.session.commit()  # 提交到数据库

        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")
    return jsonify({"message": "An error occurred while storing data!"})


@app.route('/today')
def scrape_today():
    # 初始化 XPath 规则类（这里是一个示例，你可以根据需要使用不同的规则类）
    for specific_xpath_rules in [XPathRules_medium(), XPathRules_labs(), XPathRules_nigerald(),
                                 XPathRules_zhidao(), XPathRules_sihou(), XPathRules_fanka(), XPathRules_52pojie(),
                                 XPathRules_blog(), XPathRules_anquanke(), XpathRules_t001s(), XPathRules_seck(),
                                 XPathRules_freebuf(), XPathRules_kanxue()]:
        scraper = WebScraper(specific_xpath_rules)
        # 调用爬虫的 main 方法并获取爬取结果
        scraped_items = scraper.scrape()
        # 保存数据到 SQLite 数据库
        for item in scraped_items:
            new_record = Spider_today(
                title=item.get('title'),
                url=item.get('url'),
                date=item.get('date'),
                web_name=item.get('web_name'),
                category=item.get('category'),
                now_date=item.get('now_date')
            )
            db.session.add(new_record)

        try:
            db.session.commit()  # 提交到数据库

        except Exception as e:
            print(f"An error occurred: {e}")
    return jsonify({"message": "An error occurred while storing data!"})


if __name__ == '__main__':
    app.run(debug=True)
