"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/4/28 9:58
@Filename			: ip_utils.py
@Description		: 
@Software           : PyCharm
"""


def get_client_ip(request):
    """
    获取ip
    :param request:
    :return:
    """
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""
    return regip
