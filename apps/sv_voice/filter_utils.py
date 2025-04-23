"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/10/14 10:47
@Filename			: filter_utils.py
@Description		: 
@Software           : PyCharm
"""


class DigitalHumanCloneFilter(object):
    def filter_queryset(self, request, queryset, obj):
        user_code = request.user.user_code
        queryset = queryset.filter(create_by=user_code)

        return queryset.all()
