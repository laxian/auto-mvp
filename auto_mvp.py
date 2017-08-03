#! /usr/bin/python
# encoding=utf-8

'''
通过模板，快速生成MVP框架文件
M:
    IXxxModel
    XxxModel
P:
    IXxxPresenter
    XxxPresenter
V:
    IXxxView
并在HttpConstant中添加对应的URL和KEY

使用方法：python auto_mvp.py [apiName]
'''
import create_presenter as cp
import create_model as cm