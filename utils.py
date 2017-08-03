#! /usr/bin/python
# encoding=utf-8

import json
from collections import OrderedDict
from config import mode_all as mode, api


def split_camel(str):
    if str is None or str == '':
        return []
    i, front = 1, 0
    lst = []
    while i < len(str):
        if str[i].isupper():
            lst.append(str[front:i])
            front = i
        i += 1
    lst.append(str[front:])
    return lst


def read_cfg(cfg):
    ret = []

    # 读取json接口描述
    fconfig = open(cfg)
    jarr = json.loads(fconfig.read(), object_pairs_hook=OrderedDict)

    for a in jarr:
        if not mode and api != a['apiName']:
            continue
        ret.append(parse_api_dict(a))

    return ret


def parse_api_dict(jdict):
    ret = {}
    # 1.获取apiName
    Path=''
    if 'path' in jdict:
        Path = jdict['path'].capitalize()
    apiName = jdict['apiName'].replace('.do', '')
    ApiName = Path + apiName[0].upper() + apiName[1:]
    # 2.拼接形参
    TypedParams = ''
    ParamsPair = ''
    Params = ''
    for k in jdict['params']:
        if k == 'time' or k == 'sign':
            continue
        v = jdict['params'][k]
        # print "%s %s," % (v, k)
        TypedParams += '%s %s,' % (v, k)
        ParamsPair += r'"%s", %s,' % (k, k)
        Params += r'%s, ' % (k)
    TypedParams = TypedParams.rstrip(',')
    ParamsPair = ParamsPair.rstrip(',')
    Params = Params.strip().rstrip(',')
    # 3.接口URL和KEY
    API_NAME = '_'.join(split_camel(ApiName)).upper()
    # 4.METHOD:GET OR POST?
    method = jdict['method']
    ret['apiName'] = apiName
    ret['ApiName'] = ApiName
    ret['TypedParams'] = TypedParams
    ret['ParamsPair'] = ParamsPair
    ret['Params'] = Params
    ret['API_NAME'] = API_NAME
    ret['method'] = method
    ret['path'] = Path.lower()
    return ret


def replace_all(str, dic):
    for k in dic:
        str = str.replace('{%s}' % (k), dic[k])
    return str
