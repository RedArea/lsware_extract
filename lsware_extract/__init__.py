import os
import sys
import argparse
from time import sleep
from random import randint

def _real_main(argv=None):
    parser = argparse.ArgumentParser(description="lsware_extract dummy tool")
    parser.add_argument('-type', help="select type [all, part, partial]", required=True, choices=['all', 'part', 'partial'])
    parser.add_argument('-in', help="input the path of the content file", required=True, dest='content')
    parser.add_argument('-media', help="select media [image, video, audio, mobile]", required=True, choices=['image', 'video', 'audio', 'mobile'])
    parser.add_argument('-log', help="input the path of the log file", required=True, type=argparse.FileType('a'))  # 빈 값일 시 Error 발생
    parser.add_argument('-out', help="input the path of the dna file")

    args = parser.parse_args()
    args.log.close()

    sleep(randint(0, 3))

    with open(args.log.name, 'a') as f:
        f.write(args.type + '\n')
        f.write(args.content + '\n')
        f.write(args.media + '\n')
        f.write(args.log.name + '\n')

def main(argv=None):
    try:
        _real_main(argv)
    except :
        print "exception!!!!!!!!!!"


 
# log = "{start_time}, {content}, {end_time}, {errmsg}".format(start_time=, content=args.content, end_time=, errmsg="")
# log = "{start_time}, {content}, {end_time}, {errmsg}".format(start_time=, content=args.content, end_time=, errmsg="")


# all = 
# [yyyy-mm-dd hh:mm:ss(starttime), input_file_path, yyyy-mm-dd hh:mm:ss(endtime), errmsg]
# -type all -media video -in "e:\pes\test\video\V380\369552.avi" -log "E:\pes_run\PES-2017-FF-089\log\PES-2017-FF-089_V_X3350.log" -out "E:\pes_run\PES-2017-FF-089\DNA"
# -type all -media image -in "D:\PES_TEST\SRC\image\641145" -log "D:\PES_TEST\PES-2013-FF-045\LOG\PES-2013-FF-045_I_X350.log" -out "D:\PES_TEST\PES-2013-FF-045\DNA\image"
#     -> 641145.dna 로 출력

# part= [yyyy-mm-dd hh:mm:ss(starttime), input_file_path, yyyy-mm-dd hh:mm:ss(querytime), return_value, endtime, errmsg]
# -type part -media video -in "e:\pes\test\video\V380\369552.avi" -log "E:\pes_run\PES-2017-FF-089\log\PES-2017-FF-089_V_X3310.log"
