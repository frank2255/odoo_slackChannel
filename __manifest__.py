# slack_page/__manifest__.py
{
    'name': 'Slack Integration for Res Partner',
    'version': '1.0',
    'summary': 'Integration with Slack to show messages in Res Partner',
    'author': 'Your Name',
    'license': 'LGPL-3',  # 添加這一行來明確指定授權
    'depends': ['base', 'contacts'],  # 確保包含 contacts 依賴
    'data': [
        'views/res_partner_views.xml',  # 引入視圖文件
    ],
    'installable': True,
    'application': False,
}
