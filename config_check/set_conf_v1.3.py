#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    本文件用来检测融数科技生产线上快贷的配置文件
    version 1.3
    经过三次改动，已经可以核对很多不同环境的配置文件
    在核对前，请确认标准配置文件和生产线上配置文件的路径
    也就是stand_conf 和pro_conf参数的指的路径
'''

#生产路径
stand_conf='/opt/scrpit/config.properties'
pro_conf='/opt/service/tansun/tomcat/webapps/quickloan/WEB-INF/classes/config.properties'

#测试路径
stest_conf='config.properties'
dtest_conf='config.properties1'

#存储介质
stand_dict={}
pro_dict={}


class date_format:
    def get_parameter(self,stest_conf,distc):
        with open(stest_conf,'r') as f:
            for item in f:
                if item.startswith('#'):
                    continue
                if '=' in item:
                    split_line=item.split('=')
                    distc[split_line[0].strip()]='='.join(split_line[1:]).strip()
        return distc

class diff_set:
    def set_format(self,s_dict,d_dict):
        stand_set=set(s_dict.keys())
        pro_set=set(d_dict.keys())
        count_n=0
        for i in stand_set:
            if i in pro_set:
                if s_dict[i] != d_dict[i]:
                    #print('与标准配置文件内容不一样的有： '+ i,'标准： '+stand_dict[i],'生产: '+pro_dict[i])
                    print('Different from standard configuration content : '+ i,' standard: '+s_dict[i],' production: '+d_dict[i])
                    count_n+=1

        if count_n == 0:
            print('The same as standard configuration content')

        more_diff=pro_set.difference(stand_set)
        less_diff=stand_set.difference(pro_set)
        if len(more_diff) != 0:
            print('More parameters than standard configuration files: '+ str(more_diff))
            count_n+=1
        else:
            print('Nothing')

        if len(less_diff) != 0:
            print('Parameters less than standard configuration files: '+ str(less_diff))
            count_n+=1
        else:
            print('Nothing')

        if count_n==0:
            print('Congratulations! The same as standard configuration as production configuraction')
            print('Now,You can start this project.')


if __name__=='__main__':
    print('Please confirm that the standard configuration file and production profile directory are correct.')
    print('stand_conf: ' + stand_conf)
    print('pro_conf: ' + pro_conf)
    stand_data=date_format()
    stand_data.get_parameter(stest_conf,stand_dict)
    
    pro_data=date_format()
    pro_data.get_parameter(dtest_conf,pro_dict)

    Diff_Set=diff_set()
    Diff_Set.set_format(stand_dict,pro_dict)
