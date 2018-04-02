#!/usr/bin/env python
#coding:utf-8

'''
    本文件用来检测融数科技生产线上快贷的配置文件
'''

config_path='/opt/service/tansun/tomcat/webapps/quickloan/WEB-INF/classes/config.properties'
config_test='/home/able/Test/config_check/config.properties'
config_diff='/home/able/Test/config_check/config.properties1'

with open(config_test,'r') as f:
    sfile=f.readlines()
    for item in range(len(sfile)):
        sfile[item]=sfile[item].replace(' ','')
    with open(config_diff,'r') as d1:
        dfile=d1.readlines()
        for item1 in range(len(dfile)):
            dfile[item1]=dfile[item1].replace(' ','')
        for i in dfile:
            if i not in sfile:
                print('This value is diffcult:  ' + i)
                
    
