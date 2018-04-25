# _*_ coding: utf-8 _*_
__author__ = 'xiaoke'
__date__ = '2018/4/3 19:09'

import xadmin
from .models import  CityDict, CourseOrg, Teater

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    list_display = ['name', 'desc','category', 'click_num','fav_num', 'image', 'address','city','add_time']
    search_fields = ['name', 'desc', 'category', 'click_num','fav_num', 'image', 'address','city']
    list_filter = ['name', 'desc', 'category','click_num','fav_num', 'image', 'address','city','add_time']

class TeaterAdmin(object):
    list_display = ['org', 'name', 'work_years','work_company', 'work_position', 'points','click_num','fav_num','add_time']
    search_fields = ['org__name', 'name', 'work_years','work_company', 'work_position', 'points','click_num','fav_num']
    list_filter = ['org', 'name', 'work_years','work_company', 'work_position', 'points','click_num','fav_num','add_time']

xadmin.site.register(CityDict,CityDictAdmin )
xadmin.site.register(CourseOrg,CourseOrgAdmin )
xadmin.site.register(Teater,TeaterAdmin )