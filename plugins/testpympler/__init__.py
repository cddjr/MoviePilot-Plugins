from typing import Any, List, Dict, Tuple

from pympler import tracker

from app.core.config import settings
from app.plugins import _PluginBase


class TestPympler(_PluginBase):
    # 插件名称
    plugin_name = "Pympler"
    # 插件描述
    plugin_desc = "TDB"
    # 插件图标
    plugin_icon = "Bookstack_A.png"
    # 插件版本
    plugin_version = "0.2"
    # 插件作者
    plugin_author = "cddjr"
    # 作者主页
    author_url = "https://github.com/cddjr"
    # 插件配置项ID前缀
    plugin_config_prefix = "testpympler_"
    # 加载顺序
    plugin_order = 5
    # 可使用的用户级别
    auth_level = 1

    # 私有属性
    _content = ""
    _st = None

    def init_plugin(self, config: dict = None):
        self._st = tracker.SummaryTracker()

    def get_state(self) -> bool:
        return True

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        pass
    
    def _get_summary(self):
        return self._st.create_summary()

    def get_api(self) -> List[Dict[str, Any]]:
        pass

    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        """
        拼装插件配置页面，需要返回两块数据：1、页面配置；2、数据结构
        """
        return [
            {
                'component': 'VForm',
                'content': [
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                },
                                'content': [
                                    {
                                        'component': 'VTextarea',
                                        'props': {
                                            'model': 'content',
                                            'label': 'TBD',
                                            'rows': 12
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ], {
            "enabled": False,
            "content": str(self._get_summary())
        }

    def get_page(self) -> List[dict]:
        pass

    def stop_service(self):
        """
        退出插件
        """
        pass
