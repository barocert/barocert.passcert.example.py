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
완료된 전자서명을 검증하고 전자서명값(signedData)을 반환 받습니다.
검증 함수는 전자서명 요청 함수를 호출한 당일 23시 59분 59초까지만 호출 가능합니다.
전자서명 요청 함수를 호출한 당일 23시 59분 59초 이후 검증 함수를 호출할 경우 오류가 반환됩니다.
https://developers.barocert.com/reference/pass/python/sign/api#VerifySign
"""

# 이용기관 코드
clientCode = settings.ClientCode

signVerify = PassSignVerify(        
    receiverHP = passcertService._encrypt('01012341234'),
    receiverName = passcertService._encrypt('홍길동')
)

try :
    obj = passcertService.verifySign(clientCode, '02309080230700000140000000000012', signVerify)
    print(obj.receiptID)
    print(obj.state)
    print(obj.receiverName)
    print(obj.receiverHP)
    print(obj.receiverYear)
    print(obj.receiverDay)
    print(obj.receiverGender)
    print(obj.receiverForeign)
    print(obj.receiverTelcoType)
    print(obj.signedData)
    print(obj.ci)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)