__author__ = 'liujunyuan'
#-*-coding:utf-8-*-
import linecache
import json
# ===================================

# ===================================


def txt_process(txtfile_path,filenumber,output_path,row_output):

    thetext = open(output_path,'w')
    txt_row = open(row_output,'w')

    for i in range(1,filenumber,1):
        theline = linecache.getline(txtfile_path,i)
        array_theline = theline.split(',')

        thelatitude = array_theline[1]
        thelongitude = array_theline[2]
        thetxt = array_theline[-1]
        str_i = str(i)

        thesample = [str_i,'|',thelatitude,'|',thelongitude,'|',thetxt]

        thetext.writelines(thesample)
        txt_row.writelines(thetxt)
    thetext.close()


# txtfile_path = '/Users/liujunyuan/Desktop/2015-6-20_2000.txt'
# filenumber = len(open(txtfile_path).readlines())+1
# output_path = '/Users/liujunyuan/Desktop/2000.txt'
# row_output = '/Users/liujunyuan/Desktop/row.txt'
# residue_output = '/Users/liujunyuan/Desktop/residue.txt'
# txt_process(txtfile_path,filenumber,output_path,row_output)

# def json_process():
# json_path = '/Users/liujunyuan/Desktop/result 2.txt'
#
# json_file = open(json_path).read()
# json_result = json.dumps(json_file)#str
# print json_result

# json_load = json.loads(json_file)#list
# print json_load
#
# #print a.decode('unicode-escape')
#
