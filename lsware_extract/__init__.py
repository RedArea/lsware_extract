import os
import sys
import argparse
import time
from random import randint

def _real_main(argv=None):
    parser = argparse.ArgumentParser(description="lsware_extract dummy tool")
    parser.add_argument('-type' , default=None) #, help="select type [all, part, partial]", required=True, choices=['all', 'part', 'partial'])
    parser.add_argument('-in'   , default=None, dest='content') #, help="input the path of the content file", required=True)
    parser.add_argument('-media', default=None) #, help="select media [image, video, audio, mobile]", required=True, choices=['image', 'video', 'audio', 'mobile'])
    parser.add_argument('-log'  , default=None, help="input the path of the log file", required=True, type=argparse.FileType('a'))
    parser.add_argument('-out'  , default=None) #, help="input the path of the dna file")
    args = parser.parse_args()
    
    type    = args.type.lower()
    content = args.content
    media   = args.media.lower()
    log     = args.log
    out     = args.out

    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    sleep(randint(0, 3))

    if type is None or content is None:
        log.write()## 오류 로그 포함 작성 후 종료
        sys.exit()

    if type is 'all':
        if out is None:
            log.write()## 오류 로그 포함 작성 후 종료
            sys.exit()
        else:
            if out[-1] is not '/':
                out = out + '/'
        
        dna_file_name = content.split('/')[-1]

        if media is 'image':
            dna_file_name = dna_file_name + '.dna'

        dna_path = out + '/' + dna_file_name

        if os.path.exists(dna_path):
            os.remove(dna_path)

        init_path = os.path.realpath(os.path.abspath(__file__))
        root_path_list = init_path.split(os.path.sep)[:-2]
        bin_path = os.path.join(os.path.sep.join(root_path_list), 'bin')
        dna_sample_path = os.path.join(bin_path, 'sample.dna')
        adna_file = os.path.join(out, dna_file_name + '.adna')

        with open(dna_sample_path, 'r') as dna:
            with open(adna_file, 'a') as adna:
                for i in range(randint(0, 300)):
                    line = dna.readline()
                    if not line: break
                    adna.write(line)

        vdna_file = os.path.join(out, dna_file_name + '.vdna')
        with open(dna_sample_path, 'r') as dna:
            with open(vdna_file, 'a') as vdna:
                for i in range(randint(0, 300)):
                    line = dna.readline()
                    if not line: break
                    vdna.write(line)   
        
        log.write()## 로그 작성 후 종료
        sys.exit()
    else:
        print("part")

def main(argv=None):
    try:
        _real_main(argv)
    except OSError as e:
        print "Invalid log file path.", e
    except Exception as e:
        print "exception!!!!!!!!!!", e


 
# log = "{start_time}, {content}, {end_time}, {errmsg}".format(start_time=, content=args.content, end_time=, errmsg="")
# log = "{start_time}, {content}, {end_time}, {errmsg}".format(start_time=, content=args.content, end_time=, errmsg="")


# all = 
# [yyyy-mm-dd hh:mm:ss(starttime), input_file_path, yyyy-mm-dd hh:mm:ss(endtime), errmsg]
# -type all -media video -in "e:\pes\test\video\V380\369552.avi" -log "E:\pes_run\PES-2017-FF-089\log\PES-2017-FF-089_V_X3350.log" -out "E:\pes_run\PES-2017-FF-089\DNA"
# -type all -media image -in "D:\PES_TEST\SRC\image\641145" -log "D:\PES_TEST\PES-2013-FF-045\LOG\PES-2013-FF-045_I_X350.log" -out "D:\PES_TEST\PES-2013-FF-045\DNA\image"
#     -> 641145.dna 로 출력

# part= [yyyy-mm-dd hh:mm:ss(starttime), input_file_path, yyyy-mm-dd hh:mm:ss(querytime), return_value, endtime, errmsg]
# -type part -media video -in "e:\pes\test\video\V380\369552.avi" -log "E:\pes_run\PES-2017-FF-089\log\PES-2017-FF-089_V_X3310.log"
