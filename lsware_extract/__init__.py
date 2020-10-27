import os
import sys
import argparse

def main(argv=None):
    parser = argparse.ArgumentParser(description="lsware_extract dummy tool")
    parser.add_argument('-type', help="select type [all, part, partial]", required=True, choices=['all', 'part', 'partial'])
    parser.add_argument('-in', help="input the path of the content file", required=True)
    parser.add_argument('-media', help="select media [image, video, audio, mobile]", required=True, choices=['image', 'video', 'audio', 'mobile'])
    parser.add_argument('-log', help="input the path of the log file", required=True, type=argparse.FileType('w'))
    parser.add_argument('-out', help="input the path of the dna file")

    args = parser.parse_args()
    
    with open(args.log, "w") as f:
        f.write(args.type)
        f.write(args.in)
        f.write(args.media)
        f.write(args.log)