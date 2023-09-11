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
passcertService.UseLocalTimeYN = settings.UseLocalTimeYN

"""
패스 이용자에게 문서의 전자서명을 요청합니다.
https://developers.barocert.com/reference/pass/python/sign/api#RequestSign
"""

# 이용기관 코드
clientCode = settings.ClientCode

sign = PassSign(        
    receiverHP = passcertService._encrypt('01012341234'),
    receiverName = passcertService._encrypt('홍길동'),
    receiverBirthday = passcertService._encrypt('19700101'),
    reqTitle = '전자서명 요청 메시지 제목란',
    reqMessage = passcertService._encrypt('전자서명 요청 메시지'),
    callCenterNum = '1600-9854',
    expireIn = 1000,
    token = passcertService._encrypt('전자서명테스트데이터'),
    tokenType = 'HASH',
    userAgreementYN = True,
    receiverInfoYN = True,
    originalTypeCode = 'AG',
    originalURL = 'https://www.passcert.co.kr',
    originalFormatCode = 'HTML',
    appUseYN = False,
)

try :
    obj = passcertService.requestSign(clientCode, sign)
    print(obj.receiptId)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)