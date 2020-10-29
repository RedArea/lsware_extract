import os
import sys
import argparse
import time
from random import randint

def _real_main(argv=None):
    parser = argparse.ArgumentParser(description="lsware_extract dummy tool")
    parser.add_argument('-type') #, help="select type [all, part, partial]", required=True, choices=['all', 'part', 'partial'])
    parser.add_argument('-in', dest='content') #, help="input the path of the content file", required=True)
    parser.add_argument('-media') #, help="select media [image, video, audio, mobile]", required=True, choices=['image', 'video', 'audio', 'mobile'])
    parser.add_argument('-log', help="input the path of the log file", required=True, type=argparse.FileType('a'))
    parser.add_argument('-out') #, help="input the path of the dna file")
    args = parser.parse_args()
    
    type    = args.type.lower()
    content = args.content
    media   = args.media.lower()
    log     = args.log
    out     = args.out
    errmsg  = ""

    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(randint(0, 3))

    if not type or not content:
        end_time = time.strftime('%Y-%m-%d %H:%M:%S')
        errmsg = "parameter error : {type}, {content}, {media}, {log}, {out}".format(type=type, content=content, media=media, log=log.name, out=out)
        log_msg = "{start_time}, {content}, {end_time}, {errmsg}\n".format(start_time=start_time, content=content, end_time=end_time, errmsg=errmsg)
        log.write(log_msg)
        sys.exit()

    if type is 'all':
        if not out:
            end_time = time.strftime('%Y-%m-%d %H:%M:%S')
            errmsg = "parmeter error : Missing path to save feature point file"
            log_msg = "{start_time}, {content}, {end_time}, {errmsg}\n".format(start_time=start_time, content=content, end_time=end_time, errmsg=errmsg)
            log.write(log_msg)
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
        
        end_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log_msg = "{start_time}, {content}, {end_time}, {errmsg}\n".format(start_time=start_time, content=content, end_time=end_time, errmsg=errmsg)
        log.write(log_msg)
        sys.exit()
    else:
        find_value = ""
        random_num = randint(0, 10)

        if random_num is not 0 or random_num is not 9:
            if random_num < 3:
                find_value = 1
            else:
                find_value = randint(0,100)

        elif random_num is 9:
            errmsg = "error : random number is 9" 

        query_time = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.strftime('%Y-%m-%d %H:%M:%S')
    
        if not errmsg:   
            log_msg = "{start_time}, {content}, {query_time}, {find_value}, {end_time}\n".format(start_time=start_time, content=content, query_time=query_time, find_value=find_value, end_time=end_time)
        else:
            log_msg = "{start_time}, {content}, {query_time}, {find_value}, {end_time}, {errmsg}\n".format(start_time=start_time, content=content, query_time=query_time, find_value=find_value, end_time=end_time, errmsg=errmsg)

        log.write(log_msg)
        sys.exit()

def main(argv=None):
    try:
        _real_main(argv)
    except OSError as e:
        print "Invalid log file path.", e
    except Exception as e:
        print "unhandled exception!", e

