#! /usr/bin/python
# encoding=utf-8

from constant import cfg
from constant import constant_key
from constant import constant_path
from constant import constant_url
from constant import path_const
from constant import path_model
from constant import template_impl
from constant import template_impl_get
from constant import template_int
from utils import read_cfg
from utils import replace_all

dic_list = read_cfg(cfg)

for phd in dic_list:
    print ('---->\t'+phd['API_NAME'])

    # 处理IModel
    ftem = open(template_int)
    content = ftem.read()

    created_file_name = 'I%sModel.java' % (phd['ApiName'])
    created_file = open(path_model + created_file_name, 'w+')
    created_file.write(replace_all(content, phd))
    created_file.close()

    # 处理ModelImpl
    if phd['method'].lower() == 'get':
        fimp = open(template_impl_get)
    else:
        fimp = open(template_impl)
    imp_content = fimp.read()

    create_impl_name = "%sModel.java" % (phd['ApiName'])
    create_impl = open(path_model + '/impl/' + create_impl_name, 'w+')
    create_impl.write(replace_all(imp_content, phd))
    create_impl.close()

    # 在HttpConstants里声明KEY和URL
    fconstant = open(path_const, 'r+')
    constant_content = fconstant.read()
    constant_content = constant_content.strip().strip('}')

    # 写入文件末尾
    if 'URL_%s '%(phd['API_NAME']) not in constant_content:

        fconstant.truncate()
        fconstant.seek(0)
        fconstant.write(constant_content)
        fconstant.write('\n\t// v1.2 auto-generate\n')

        add_path=''
        if 'path' in phd and phd['path'] != '':
            path = phd['path']
            add_path=' + %s'%(path.upper())
            if constant_path%(path.upper(), path) not in constant_content:
                fconstant.write(constant_path%(path.upper(), path))
        fconstant.write(constant_key%(phd['API_NAME'], add_path, phd['apiName']))
        fconstant.write(constant_url%(phd['API_NAME'], phd['apiName']))
        fconstant.write('\n}')
    else:
        print ('---> skip add %s IN HttpConstant.java'%(phd['API_NAME']))
        print (constant_key)
    fconstant.close()
