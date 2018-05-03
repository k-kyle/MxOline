# _*_ coding: utf-8 _*_
__author__ = 'xiaoke'
__date__ = '2018/5/2 19:10'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name="course_detail"),
]
