# -*- coding: utf-8 -*-
# @Time    : 2024/08/12 16:56 
# @Author  : gzy

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Spider_info(db.Model):
    __tablename__ = 'spider_info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=False, )
    date = db.Column(db.String, nullable=False)
    web_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    now_date = db.Column(db.String(100), nullable=True)


class Spider_today(db.Model):
    __tablename__ = 'spider_today'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String, nullable=False)
    web_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    now_date = db.Column(db.String(100), nullable=True)
