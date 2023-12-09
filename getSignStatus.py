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
전자서명 요청 후 반환받은 접수아이디로 인증 진행 상태를 확인합니다.
상태확인 함수는 전자서명 요청 함수를 호출한 당일 23시 59분 59초까지만 호출 가능합니다.
전자서명 요청 함수를 호출한 당일 23시 59분 59초 이후 상태확인 함수를 호출할 경우 오류가 반환됩니다.
https://developers.barocert.com/reference/pass/python/sign/api#GetSignStatus
"""

# 이용기관 코드
clientCode = settings.ClientCode

try :
    obj = passcertService.getSignStatus(clientCode, '02309080230700000140000000000012')
    print(obj.clientCode)
    print(obj.receiptID)
    print(obj.state)
    print(obj.requestDT)
    print(obj.completeDT)
    print(obj.expireDT)
    print(obj.rejectDT)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)