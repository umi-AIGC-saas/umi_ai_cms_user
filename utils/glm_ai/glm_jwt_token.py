"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/7/11 14:06
@Filename			: glm_jwt_token.py
@Description		: 
@Software           : PyCharm
"""
import time

import cachetools.func
import jwt

API_TOKEN_TTL_SECONDS = 3 * 60

CACHE_TTL_SECONDS = API_TOKEN_TTL_SECONDS - 30


@cachetools.func.ttl_cache(maxsize=10, ttl=CACHE_TTL_SECONDS)
def generate_token(apikey: str):
    try:
        api_key, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid api_key", e)

    payload = {
        "api_key": api_key,
        "exp": int(round(time.time() * 1000)) + API_TOKEN_TTL_SECONDS * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )
