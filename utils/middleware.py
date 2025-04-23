"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/5/31 13:34
@Filename			: middleware.py
@Description		: 
@Software           : PyCharm
"""
import logging
import json
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if str(request.method).upper() == "GET":
            return
        try:
            msg = '{}-{}\n GET {}\n POST {}'.format(request.path, request.method, json.dumps(request.GET), request.body.decode('utf8'))
            logger.info(msg)
        except Exception as e:
            pass
