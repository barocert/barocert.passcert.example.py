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
패스 이용자에게 본인인증을 요청합니다.
https://developers.barocert.com/reference/pass/python/identity/api#RequestIdentity
"""

# 이용기관 코드
clientCode = settings.ClientCode

identity = PassIdentity(        
    receiverHP = passcertService._encrypt('01012341234'),
    receiverName = passcertService._encrypt('홍길동'),
    receiverBirthday = passcertService._encrypt('19700101'),
    reqTitle = '본인인증 요청 메시지 제목란',
    reqMessage = passcertService._encrypt('본인인증 요청 메시지'),
    callCenterNum = '1600-9854',
    expireIn = 1000,
    token = passcertService._encrypt('본인인증요청토큰'),
    userAgreementYN = True,
    receiverInfoYN = True,
    appUseYN = False
)

try :
    obj = passcertService.requestIdentity(clientCode, identity)
    print(obj.receiptId)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)