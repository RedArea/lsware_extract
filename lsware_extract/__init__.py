import os
import sys
import argparse

def main(argv=None):
    parser = argparse.ArgumentParser(description="lsware_extract dummy tool")
    parser.add_argument('-type', help="select type [all, part, partial]", required=True, choices=['all', 'part', 'partial'])
    parser.add_argument('-in', help="input the path of the content file", required=True, dest='content')
    parser.add_argument('-media', help="select media [image, video, audio, mobile]", required=True, choices=['image', 'video', 'audio', 'mobile'])
    parser.add_argument('-log', help="input the path of the log file", required=True, type=argparse.FileType('a'))
    parser.add_argument('-out', help="input the path of the dna file")

    args = parser.parse_args()
    args.log.close()

    with open(args.log.name, 'a') as f:
        f.write(args.type + '\n')
        f.write(args.content + '\n')
        f.write(args.media + '\n')
        f.write(args.log.name + '\n')
