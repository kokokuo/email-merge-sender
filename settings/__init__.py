# -*- coding:utf-8 -*-
import os
"""
設定檔
"""
current_config = __import__(os.environ.get('ENV','dev'),globals(),locals(),'Conifg')
current_config = getattr(current_config, 'Config')
