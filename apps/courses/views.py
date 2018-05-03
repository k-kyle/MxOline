# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger

from operation.models import UserFavorite
from .models import Course, CourseResource


# Create your views here.

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        # 热门课程
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


class CourseDetailView(View):
    """
    课程详情页
    """

    def get(self, request, course_id):
        course = Course.objects.get(pk=int(course_id))
        # 增加课程点击数
        course.click_num += 1
        course.save()

        # 是否收藏课程
        has_fav_course = False

        # 是否收藏机构
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        # 相关课程推荐
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, 'course-detail.html', {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
        })


class CourseInfoView(View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
        # # 查询用户是否已经关联了该课程
        # user_courses = UserCourse.objects.filter(user=request.user, course=course)
        # if not user_courses:
        #     user_course = UserCourse(user=request.user, course=course)
        #     user_course.save()
        #
        # user_cousers = UserCourse.objects.filter(course=course)
        # user_ids = [user_couser.user.id for user_couser in user_cousers]
        # all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # # 取出所有课程id
        # course_ids = [user_couser.course.id for user_couser in all_user_courses]
        # # 获取学过该用户学过其他的所有课程
        # relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "course_resources": all_resources,
            # "relate_courses": relate_courses
        })
