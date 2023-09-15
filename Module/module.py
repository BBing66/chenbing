from happy_python import HappyLog, get_exit_code_of_cmd, HappyConfigBase
import os
import json
import time
from happy_python.happy_log import HappyLogLevel
from os.path import join, dirname

hlog = HappyLog.get_instance()


# basic_config_info = {}

website_details = []

# def get():
#     #
#     node = '/usr/bin/node'
#     js = '/home/cb/workTest/pythonProject/Module/zymod_browser.js'
#     chrome = '/usr/bin/google-chrome-stable'
#     url = 'https://www.baidu.com'
#     json2 = '/home/cb/workTest/pythonProject/Module/2023_09_12_16_09_59.json'
#     jpg = '/home/cb/workTest/pythonProject/Module/2023_09_12_16_09_59.jpg'
#     # nodejs 环境变量
#     node_modules_path = '/home/cb/workspace/ZhiYanModule/zhiyan-mod-browser/node_modules'
#     # 打印命令
#
#     node_js_command = '%s %s %s %s %s %s' % (node, js, chrome, url, json2, jpg)
#     hlog.info(node_js_command)
#
#
#     os.putenv('NODE_PATH', node_modules_path)
#     code = get_exit_code_of_cmd(cmd=node_js_command, is_show_error=True, is_show_output=True)
#     os.unsetenv('NODE_PATH')
#
#     if code != 0:
#         return "error"
#
#     time.sleep(1)
# #  打开sion 读取指定信息 获取url请求个数
#     with open(json2) as f:
#         log_entries = json.load(f)['log']['entries']
#
#         for i in log_entries:
#             website_details.append(i['request']['url'])
#
#
#
#     hlog.info(website_details)
#     hlog.info(len(website_details))





import base64
import json
import os
import time
from dataclasses import dataclass
from datetime import datetime
from os.path import join, dirname
from pathlib import Path
from typing import List

from happy_python import HappyLog, HappyConfigParser, HappyDatetimeFormat
from happy_python import get_exit_code_of_cmd, datetime_to_str
from zymod import Zymod
from zymod.event import ZyInternalEvent, ZyEventLevel
from zymod.zymod import upload_zy_exception_event
from zymod.zymod_config import LoadCustomizeZymodConfig, LoadPublicZymodConfig

hlog = HappyLog.get_instance()
basic_config_info = {}

__mod_config_file_path__ = '/home/cb/workTest/pythonProject/conf/module.conf'

class Config(HappyConfigBase):
    def __init__(self):
        super().__init__()

        self.section = 'cbmod'
        self.node_exec_path = ''
        self.node_exec_script_path = ''
        self.google_chrome_path = ''
        self.node_js_command_line_parameters = ''
        self.env_node_modules_path = ''
        self.browser_url = ''
        self.json_path = ''
        self.jpg_path = ''


def main():
    conf_path = __mod_config_file_path__
    browser_conf = Config()
    HappyConfigParser.load(conf_path,browser_conf)

    node_path = browser_conf.node_exec_path
    js_path = browser_conf.node_exec_script_path
    chrome_path = browser_conf.google_chrome_path
    url = browser_conf.browser_url
    json_path = browser_conf.json_path
    jpg_path = browser_conf.jpg_path

    node_modules_path = browser_conf.env_node_modules_path

    node_js_command  = '%s %s %s %s %s %s' % (node_path, js_path, chrome_path, url, json_path, jpg_path)

    hlog.info(node_js_command)

    os.putenv('NODE_PATH',node_modules_path)
    code = get_exit_code_of_cmd(cmd=node_js_command, is_show_error=True, is_show_output=True)
    os.unsetenv('NODE_PATH')

    if code != 0:
        return "error"

    time.sleep(3)

    with open(json_path) as j:
        log_entries = json.load(j)['log']['entries']
        for i in log_entries:
            website_details.append(i['request']['url'])

    hlog.info(website_details)
    hlog.info(len(website_details))

if __name__ == '__main__':
     main()
