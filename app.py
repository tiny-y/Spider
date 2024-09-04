from flask import Flask, jsonify, request
from models.models import db, Spider_today, Spider_info
from spider.spider_keyword import *
from spider.model import *

app = Flask(__name__)


# 初始化数据库
def init_sqlite():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite3.db"  # 连接数据库
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()


def scrape_and_store(scraper_class, model_class):
    """
    通用函数用于爬取数据并存储到数据库
    :param scraper_class: 爬虫类
    :param model_class: 数据模型类
    :return: 成功消息或错误消息
    """
    # 爬取数据
    scraped_items = scraper_class.scrape() if hasattr(scraper_class, 'scrape') else scraper_class.mian()

    # 保存数据到 SQLite 数据库
    for item in scraped_items:
        new_record = model_class(
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
        return "数据保存成功！"
    except Exception as e:
        db.session.rollback()  # 回滚事务
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"


@app.route("/")
def index():
    return "<h1>这是首页</h1>"


@app.route('/searched/<search>')
def scrape_data(search):
    # 初始化 XPath 规则类
    for specific_xpath_rules in [XpathRules_freebuf(search), XpathRules_kanxue(search), XpathRules_anquanke(search),
                                 XpathRules_blog(search), XpathRules_seck(search), XpathRules_medium(search),
                                 XpathRules_sihou(search), XpathRules_zhidao(search), XpathRules_mcafee(search)]:
        spider = SpiderForKey(specific_xpath_rules)
        result = scrape_and_store(spider, Spider_info)
    return jsonify({"message": "搜索并保存数据成功！"})


@app.route('/today')
def scrape_today():
    # 初始化 XPath 规则类
    for specific_xpath_rules in [XPathRules_medium(), XPathRules_labs(), XPathRules_nigerald(), XPathRules_zhidao(),
                                 XPathRules_sihou(), XPathRules_fanka(), XPathRules_52pojie(),
                                 XPathRules_blog(), XPathRules_anquanke(), XPathRules_t001s(), XPathRules_seck(),
                                 XPathRules_freebuf(), XPathRules_kanxue()]:
        scraper = WebScraper(specific_xpath_rules)
        result = scrape_and_store(scraper, Spider_today)
        if "error" in result:
            return jsonify({"message": result}), 500
    return jsonify({"message": "爬取并保存数据成功！"})


@app.route('/query', methods=['GET'])
def query_info():
    search_keyword = request.args.get('keyword', '')
    # 如果用户没有提供关键词，返回错误信息
    if not search_keyword:
        return jsonify({"error": "请提供一个关键词进行查询！"}), 400

    # 进行模糊查询操作
    try:
        # 在 Spider_info 表中查询标题中包含关键词的记录
        results_info = Spider_info.query.filter(Spider_info.title.like(f"%{search_keyword}%")).all()
        # 在 Spider_today 表中查询标题中包含关键词的记录
        results_today = Spider_today.query.filter(Spider_today.title.like(f"%{search_keyword}%")).all()

        # 格式化结果为JSON
        result_data = {
            "Spider_info_results": [result.to_dict() for result in results_info],
            "Spider_today_results": [result.to_dict() for result in results_today]
        }
        return jsonify(result_data), 200

    except Exception as e:
        print(f"查询错误: {e}")
        return jsonify({"error": f"查询时发生错误: {str(e)}"}), 500


if __name__ == '__main__':
    init_sqlite()
    app.run(debug=True)
