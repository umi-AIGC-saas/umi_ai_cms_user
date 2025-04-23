"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/5/17 16:00
@Filename			: urls.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import path

from apps.sp_prompts.views import prompts_views

urlpatterns = [
    path("type_list", prompts_views.Prompts.as_view({"get": "type_list"})),
    path("prompts", prompts_views.Prompts.as_view({"get": "list", "post": "create"})),
    path("recommend", prompts_views.Prompts.as_view({"get": "recommend_list", "post": "recommend_add"})),
]