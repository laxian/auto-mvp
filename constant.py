import sys

reload(sys)
sys.setdefaultencoding('utf8')

#通过是否带命令行参数，确定全部生成，还是单个生成
mode_all, api = True, ''
if len(sys.argv) == 1:
    mode_all = True
else:
    mode_all = False
    api = sys.argv[1]

project_root = '/Users/leochou/StudioProjects/bcm/'
project_src = 'app/src/main/java/com/ett/bcm/'

path_const = project_root + project_src + 'constant/HttpConstant.java'

# M-V-P dir
path_pres = project_root + project_src + 'presenter/'
path_view = project_root + project_src + 'page/view/'
path_model = project_root + project_src + 'model/'

# template file path
template_int = project_root + 'auto-mvp/IApiNameModel.txt'
template_impl = project_root + 'auto-mvp/ApiNameModel.txt'
template_impl_get = project_root + 'auto-mvp/ApiNameModel_Get.txt'
template_pres = project_root + 'auto-mvp/ApiNamePresenter.txt'
template_ipres = project_root + 'auto-mvp/IApiNamePresenter.txt'
template_view = project_root + 'auto-mvp/IApiNameView.txt'

# template declaration sentence
constant_key = '\tpublic static final String URL_%s = dev_base%s + "%s.do";\n'
constant_url = '\tpublic static final String KEY_%s = "%s.do";\n'
constant_path = '\tpublic static final String %s = "%s/";\n'

# api config json
cfg = project_root + 'auto-mvp/api.json'