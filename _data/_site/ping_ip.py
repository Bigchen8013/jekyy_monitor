from http.client import OK
import os
import re

ip_list = []

# 读取ip地址
with open("./ip_list.yml") as rf:
    lines = rf.readlines()

    for line in lines:
        if len(line) == 0:
            continue
        if line.startswith("-"):
            line = line.split(":")
            print("此时的line：",line)
            ip = line[1].strip()     # 获取文件中的ip地址
            print("获取到的IP：",ip)
            ip_list.append(ip)

    buffer = ""
    # 将结果重新写入到yml文件夹中
    for ip in ip_list:
        result = ""
        # 使用ping命令进行监控，查看是否能够返回包
        a = os.system(f"ping -c4 {ip} > /dev/null")    # 返回4个包结果
        if a == 0:
            result = "ok"
        if a == 256:
            result = "fail"
        buffer += rf"- ip: {ip} \n"
        buffer += rf"  status: {result} \n"
        buffer += rf"\n"
    print(buffer)



# Gemfile.lock
# Gemfile