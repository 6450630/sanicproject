# -*- coding: utf-8 -*-

from sanic.response import json


class SetStatusCode():
    def __init__(self) -> None:
        self.status_code = {
            "success":{"code":20000,"msg":"成功"},
            "param_error":{"code":20001,"msg":"参数错误"},
            "request_error":{"code":20002,"msg":"请求类型错误"},
            "type_error":{"code":20003,"msg":"内部运行错误"}
        }
    
    def success(self,data: dict,request: tuple, status: int) -> json:
        res = self.status_code["success"]
        if data:
            res["data"] = data
        res["request_id"] = str(request.id)
        return json(res,status=status)