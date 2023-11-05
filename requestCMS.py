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
패스 이용자에게 자동이체 출금동의를 요청합니다.
https://developers.barocert.com/reference/pass/python/cms/api#RequestCMS
"""

# 이용기관 코드
clientCode = settings.ClientCode

cms = PassCMS(        
    receiverHP = passcertService._encrypt('01012341234'),
    receiverName = passcertService._encrypt('홍길동'),
    receiverBirthday = passcertService._encrypt('19700101'),
    reqTitle = '출금동의 요청 메시지 제목',
    reqMessage = passcertService._encrypt('출금동의 요청 메시지'),
    callCenterNum = '1600-9854',
    expireIn = 1000,
    userAgreementYN = True,
    receiverInfoYN = True,
    bankName = passcertService._encrypt('국민은행'),
    bankAccountNum = passcertService._encrypt('19-******-1231'),
    bankAccountName = passcertService._encrypt('홍길동'),
    bankServiceType = passcertService._encrypt('CMS'),
    bankWithdraw = passcertService._encrypt('1,000,000원'),
    appUseYN = False,
)

try :
    obj = passcertService.requestCMS(clientCode, cms)
    print(obj.receiptID)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)