__author__ = 'liujunyuan'
# -*- coding:utf-8 -*-
import linecache
import urllib2
import time
import urllib
import tx
import json
import txt_process

# locl file parameters
# test_path = '/Users/liujunyuan/Desktop/101.txt'
txtfile_path = '/Users/liujunyuan/Desktop/2015-6-20_2000.txt'
output_path = '/Users/liujunyuan/Desktop/2000.txt'
row_output = '/Users/liujunyuan/Desktop/row1.txt'
filenumber = len(open(row_output).readlines())+1


# ======================================================================
# txt_process.txt_process(txtfile_path,filenumber,output_path,row_output)
# ======================================================================

# # upload parameters setting
URL = 'https://wenzhi.api.qcloud.com/v2/index.php?'
SecretID = 'AKIDcOaWRM71FBW4GJpupgXkP8uG4oAUJrIQ'
SecretKey = 'n3iDvouVoNhL9ThdhBLd5S2ryiteBOrw'
method = 'TextClassify'
time_sign = int(time.time())
region = 'gz'
res_output = open('/Users/liujunyuan/Desktop/result.txt','w')

for i in range(1,filenumber,1):
    thecontent = linecache.getline(row_output,i)
    # print thecontent
    thecontent = thecontent.strip('\n')
    theAutograph = tx.getSignature(method,region,SecretID,time_sign,thecontent,SecretKey)
    # print theAutograph
    #get data from tx
    try:
        req = urllib2.Request(URL,theAutograph)

        res_data = urllib2.urlopen(req)
        res = res_data.read()
        json_res = json.loads(res)#<type 'dict'>
    # print json_res
    # print json_res["classes"]
        res_outputdata = str(i) + '|' +str(json_res['classes'][0]).decode('unicode-escape')
        print (res_outputdata)
    except:
        print str(i) + 'no return'
        continue
    # print type(res_outputdata)
    # # sorted(json_res,key=)
    # # print json_res
    #
    # res_output.write(str(res_outputdata))

print 'done'
