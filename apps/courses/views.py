# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger

from .models import Course


# Create your views here.

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        #热门课程
        hot_courses = Course.objects.all().order_by("-click_num")[:3]
        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by("-students")
            elif sort == 'hot':
                all_courses = all_courses.order_by("-click_num")

        # 公开课数量
        course_nums = all_courses.count()
        # 对公开课进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 3是每页显示的数量
        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses,
        })
