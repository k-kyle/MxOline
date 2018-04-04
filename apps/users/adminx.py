# _*_ coding: utf-8 _*_
__author__ = 'xiaoke'
__date__ = '2018/4/3 15:08'

import xadmin
from xadmin import views
from models import EmailVerifyRecord,Banner,channel

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "成蹊运维后台"
    site_footer = "成蹊运维后台"
    #菜单折叠开关
    # menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display = ['id', 'code', 'email', 'send_type', 'send_time']
    search_fields = ['id', 'code', 'email', 'send_type']
    list_filter = ['id', 'code', 'email', 'send_type', 'send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

class ChannelAdmin(object):
    list_display = ['id','name','md5sum','gate_ip','gate_port','platform','in_use','dns_push_date','modify_date']
    search_fields = ['id','name','md5sum','gate_ip','gate_port','platform','in_use']
    list_filter = ['id','name','md5sum','gate_ip','gate_port','platform','in_use','dns_push_date','modify_date']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(channel, ChannelAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)