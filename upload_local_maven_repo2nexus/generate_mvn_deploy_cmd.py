#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import re

def write_file(path,logobj,repo_url,repo_id, maven_settings_file):
    count = 0
    #print path
    for fpathe,dirs,fs in os.walk(path):
        #print fpathe,dirs,fs
        for f in fs:
            if f.endswith(".pom"):
                jarname = f[0:-4]+".jar"
                jarpath= os.path.join(fpathe,jarname)
                pom = os.path.join(fpathe,f)
                if not os.path.isfile(jarpath):
                    # files no exist continue
                    continue
                info = get_pom_info(pom)
                if info:
                    groupId=info[0]
                    artifactId=info[1]
                    version=info[2]
                    deploy_common = "mvn deploy:deploy-file -DgroupId=%s -DartifactId=%s -Dversion=%s -Dpackaging=jar -Dfile=%s -Durl=%s -DrepositoryId=%s --settings=%s\n" % (groupId,artifactId,version,jarpath,repo_url,repo_id, maven_settings_file)
                    logobj.write(deploy_common)
                    print("生成命令 %d ：%s" % (count, deploy_common))
                else:
                    print ("ERROR: ",f)

def get_pom_info(file):
    #print file
    file_object = open(file,'r', encoding='UTF-8')
    n = 0
    xlist = []
    try:
        while True:
            line = file_object.readline()
            #print line
            
            ret = re.search(r'<groupId>(.*?)</groupId>',line)
            if ret:
                groupId = ret.group(1)
                #print 'groupid '+groupId
                xlist.append(groupId)
            
            ret = re.search(r'<artifactId>(.*?)</artifactId>',line)
            if ret:
                artifactId = ret.group(1)
                xlist.append(artifactId)

            ret = re.search(r'<version>(.*?)</version>',line)
            if ret:
                version = ret.group(1)
                xlist.append(version)

            n = n+1
            if n== 40:
                break
    finally:
        file_object.close()
    return xlist
    

deploy_commons_io = open('C:output.txt', 'w', encoding='UTF-8')
local_repo = 'F:/xusanduo/maven/repository2' # 本地仓库
maven_settings_file = 'F:/xusanduo/maven/apache-maven-3.3.9/conf/settings.xml' # 指定maven setting.xml 文件
repo_url = 'http://59.32.1.48:9999/repository/3rd-part/' # 建议直接从nexus web界面copy，以免写错
repo_id = '3rd-part' # 和 maven_settings_file 中的某个server的id
write_file(local_repo,deploy_commons_io, repo_url, repo_id, maven_settings_file) # 运行生成maven命令的方法
deploy_commons_io.close() # 关闭资源
