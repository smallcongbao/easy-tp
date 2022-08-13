from mcdreforged.api.all import *


def on_user_info(server: PluginServerInterface, info: Info):
    if info.content == '!!example':
        server.reply(info, 'example!!')
