from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, info : Info):
    pass


def on_user_info(server: PluginServerInterface, info: Info):
    if info.content == '!!example':
        server.reply(info, 'example!!')
