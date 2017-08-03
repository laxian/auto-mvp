#! /usr/bin/python
# encoding=utf-8

from config import cfg
from config import path_pres
from config import path_view
from config import template_ipres
from config import template_pres
from config import template_view
from utils import read_cfg
from utils import replace_all

dic_list = read_cfg(cfg)

for phd in dic_list:

    # 1.读取presenter模板
    f_pres = open(template_pres)
    cont_pres = f_pres.read()

    # 生成Presenter
    out_path_pres = '%s/impl/%sPresenter.java'%(path_pres, phd['ApiName'])
    fp = open(out_path_pres, 'w+')
    fp.write(replace_all(cont_pres,phd))
    fp.close()

    # 2.读取IPresenter接口模板
    f_ipres = open(template_ipres)
    cont_ipres = f_ipres.read()

    # 生成IPresenter
    out_path_ipres = '%s/I%sPresenter.java'%(path_pres, phd['ApiName'])
    fip = open(out_path_ipres, 'w+')
    fip.write(replace_all(cont_ipres,phd))
    fip.close()

    # 2.读取IView模板
    f_iview = open(template_view)
    cont_iview = f_iview.read()

    # 生成IView
    out_path_iview = '%s/I%sView.java'%(path_view, phd['ApiName'])
    fv = open(out_path_iview, 'w+')
    fv.write(replace_all(cont_iview,phd))