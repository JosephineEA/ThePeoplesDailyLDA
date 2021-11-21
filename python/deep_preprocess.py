import re

f=open('/Users/songqiao/code/MATLAB/期末作业/rmrb3/rmrb3/proc_data.csv','r')
# 文件路径
alllines=f.readlines()
f.close()
f=open('/Users/songqiao/code/MATLAB/期末作业/rmrb3/rmrb3/proc_data.csv','w+')
# 文件路径
for eachline in alllines:
    a=re.sub('0','',eachline) # 此处为需删去字符
    f.writelines(a)
f.close()