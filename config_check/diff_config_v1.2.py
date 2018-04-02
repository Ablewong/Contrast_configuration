#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    本文件用来检测融数科技生产线上快贷的配置文件
    version 1.2
'''


#生产环境
dfile='/opt/service/tansun/tomcat/webapps/WEB-INF/classes/config.properties'
sfile='/opt/script/config.properties'

#测试地址
testdfile='con.p'
testsfile='con.p1'

ddic={}
sdic={}
diffcult={}
beyond={}
noincludeC={}

class data_format:
    def parameter(self,testd,ddict):
        with open(testd,'r') as f:
            dfileline=f.readlines()
            for item in dfileline:
                if item.startswith('#'):
                    continue
                if '=' in item:
                    key1=item.split('=')
                    ddict[key1[0]]='='.join(key1[1:]).strip()
        return ddict

class diff_file:
    def diff_conf(self,standard,online,diffcult):
        for i in standard:
            for j in online:
                if i == j:
                    if standard[i] != online[j]:
                        diffcult[j] = online[j]
                if j not in standard:
                    beyond[j] = online[j]
                
                if i not in online:
                    noincludeC[i] = standard[i]
        return diffcult,beyond,noincludeC



if __name__=='__main__':
    dt_format=data_format()
    dt_format.parameter(testdfile,ddic)
    #print(ddic)
    dt_format.parameter(testsfile,sdic)
    #print(sdic)
    df_cnf=diff_file()
    df_cnf.diff_conf(ddic,sdic,diffcult)
    if diffcult:
        print('与标准的配置文件不同的地方有：')
        print(diffcult)

    if beyond:
        print('线上配置文件比标准多的参数有：')
        print(beyond)

    if noincludeC:
        print('线上配置文件比标准少的参数有：')
        print(noincludeC)

