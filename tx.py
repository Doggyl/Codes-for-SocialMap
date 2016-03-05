# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
import random
import hmac
import hashlib
import base64

# SecretID = 'AKIDcOaWRM71FBW4GJpupgXkP8uG4oAUJrIQ'
# SecretKey = 'n3iDvouVoNhL9ThdhBLd5S2ryiteBOrw'
# method = 'TextClassify'
# url = 'wenzhi.api.qcloud.com'
# time_sign = int(time.time())
#
# region = 'gz'
# thecontent = ' //@团魂满到要溢出来的望夫蛋:马//@小六也想要一个饼干: //@阿菜错了://@红烧打菜包: 赞//@发钱吗:真的好赞 //@TF饭圈暖心日常:#TFBOYS# 好！帅！啊！让我安静的做一个妈妈粉好吗？？'
# path = '/v2/index.php'

def getSignature(method,region,SecretID,time_sign,thecontent,SecretKey):

    url = 'wenzhi.api.qcloud.com'
    path = '/v2/index.php'
    nonce = random.randint(10,99999)

    Signature = 'Action'+'='+method+'&'+'Nonce'+'='+str(nonce)+'&'+'Region'+'='+region+'&'+'SecretId'+'='+SecretID+'&'+'Timestamp'+'='+str(time_sign)+'&'+'content'+'='+'\''+thecontent+'\''

    gettheSignature = "POST" + url + path +'?'+ Signature
    # =========================================================================================================
    # Signature = hmac.new(SecretKey,getSignature,hashlib.sha1).digest().encode('base64').rstrip()
    # print Signature
    # =========================================================================================================
    thesignature = base64.b64encode(hmac.new(SecretKey, gettheSignature, digestmod=hashlib.sha1).digest())

    the_uni_signature = urllib.quote(thesignature)
    # print Signature
    # print gettheSignature
    # print thesignature
    # print the_uni_signature
    return 'Action'+'='+method+'&'+'Nonce'+'='+str(nonce)+'&'+'Region'+'='+region+'&'+'SecretId'+'='+SecretID+'&'+'Timestamp'+'='+str(time_sign)+'&'+'Signature'+'='+the_uni_signature+'&'+'content'+'='+'\''+thecontent+'\''
# signature = getSignature(method,region,SecretID,time_sign,thecontent,SecretKey)
# print signature
# URL = 'https://wenzhi.api.qcloud.com/v2/index.php?'
#
# req = urllib2.Request(URL,signature)
# print req
#
# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print res
