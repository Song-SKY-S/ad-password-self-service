"""
Created by auto_sdk on 2019.07.01
"""
from api.base import RestApi


class OapiImpaasConverstionCreateo2oRequest(RestApi):
    def __init__(self, url=None):
        RestApi.__init__(self, url)
        self.request = None

    def getHttpMethod(self):
        return 'POST'

    def getapiname(self):
        return 'dingtalk.oapi.impaas.converstion.createo2o'