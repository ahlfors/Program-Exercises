
'''

[Example]
input:  (auto)Calorimetry- Crash Course Chemistry #19.srt
output:   19. Calorimetry- Crash Course Chemistry #19.srt

input:  (auto)Nuclear Chemistry- Crash Course Chemistry #38.srt
output:   38. Nuclear Chemistry- Crash Course Chemistry #38.srt


[Usage]
1. This program need Used in conjunction with "Youtube Auto Subtitle Downloader"
( http://userscripts.org/scripts/show/168581 )
this script can download youtube auto subtitle.
download file name will be "(auto)<something>.srt"
like: (auto)The Cold War- Crash Course US History #37.srt

2. Double click this .py file. Execute it.




[Chinese]
这个程序用于批量处理 Crash Course 频道的自动字幕.
批量处理那些文件名. 例子上面有.
本程序需要和 Youtube Auto Subtitle Downloader 搭配使用.
( http://userscripts.org/scripts/show/168581 )

'''


import glob # for get filename.
import os   # for rename file.


filename_list = glob.glob("(auto)*.srt")
#
# get all .srt file startswith (auto).
#


#
# loop and rename.
#
for filename in filename_list:
    try:
        number = filename.split("#")[1].split(".")[0]
        # get the number.
            
        new_filename = number + ". " + filename.replace("(auto)", "")
        # get new file name.
            
        os.rename(filename, new_filename)
        # rename file.
    except:
        print ("rename " + filename + " fail.")



#
# told user everything is done.
#
print ("Program Execution is complete.")






