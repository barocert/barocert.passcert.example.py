# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import settings
from datetime import datetime
from barocert import *

passcertService = PasscertService(settings.LinkID, settings.SecretKey)
passcertService.IPRestrictOnOff = settings.IPRestrictOnOff
passcertService.UseStaticIP = settings.UseStaticIP

"""
패스 이용자에게 간편로그인을 요청합니다.
https://developers.barocert.com/reference/pass/python/login/api#RequestLogin
"""

# 이용기관 코드
clientCode = settings.ClientCode

login = PassLogin(        
    receiverHP = passcertService._encrypt('01012341234'),
    receiverName = passcertService._encrypt('홍길동'),
    receiverBirthday = passcertService._encrypt('19700101'),
    reqTitle = '간편로그인 요청 메시지 제목',
    reqMessage = passcertService._encrypt('간편로그인 요청 메시지'),
    callCenterNum = '1600-9854',
    expireIn = 1000,
    token = passcertService._encrypt('간편로그인 요청 원문'),
    userAgreementYN = True,
    receiverInfoYN = True,
    appUseYN = False
    # telcoType = 'SKT',
    # deviceOSType = 'IOS'
)

try :
    obj = passcertService.requestLogin(clientCode, login)
    print(obj.receiptID)
    print(obj.scheme)
    print(obj.marketUrl)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)