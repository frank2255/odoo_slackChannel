# slack_page/models/slack_message.py
import logging
from odoo import models, fields, api
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'  # 擴展 res.partner 模型

    # 新增字段
    slack_channel_id = fields.Text(string="Slack Channel ID", readonly=True)
    slack_messages = fields.Text(string="Slack Messages", readonly=True)

    @api.model
    def fetch_slack_messages(self):
        # 從系統參數獲取 Slack Token
        slack_token = self.env['ir.config_parameter'].sudo().get_param('slack_BOT_token')
        slack_channel_id = self.env['ir.config_parameter'].sudo().get_param('Slack_channel_id')
        client = WebClient(token=slack_token)

        try:
            # 獲取 Slack 頻道歷史記錄
            result = client.conversations_history(channel=self.slack_channel_id)
            messages = result["messages"]

            # 將訊息組合為顯示文本
            formatted_messages = "\n".join([msg.get('text') for msg in messages])
            self.slack_messages = formatted_messages  # 將訊息儲存在字段中
            logger.info("{} messages found in {}".format(len(messages), slack_channel_id))
        except SlackApiError as e:
            logger.error("Error fetching Slack messages: {}".format(e))