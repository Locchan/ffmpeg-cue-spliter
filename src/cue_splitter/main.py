#!/usr/bin/env python

import argparse
from cueparser import CueSheet
import os

from cue_splitter.utils.ffmpeg import encode_cue
from cue_splitter.utils.utils import check_args

version = 1

def main():
    argParser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    argParser.add_argument("-v", "--version", help="Display version and license info.", action='store_true')
    argParser.add_argument("-p", "--path", help="Path to the .cue file or directory with .cue file(s).", type=str)
    argParser.add_argument("-o", "--output-path", help="Output path. Default is the path from --path.", type=str)
    argParser.add_argument("-b", "--output-bitrate", help="Bitrate of the output (kbps). Default is 320kbps.", type=int, default=320)
    argParser.add_argument("-f", "--output-format", help="Output format. Default is mp3.", type=str, default="mp3")
    argParser.add_argument("-a", "--additional-ffmpeg-params", help="Additional parameters to pass to ffmpeg while encoding. Default: '-nostdin'", type=str, default="-nostdin")
    argParser.add_argument("-e", "--encoding", help=".cue file encoding. Default is utf-8.", type=str, default="utf-8")
    argParser.add_argument("-c", "--custom-ffmpeg-path", help="Custom path for ffmpeg executable.", type=str)
    argParser.add_argument("-t", "--filename-template", help="Template for resulting filenames. Default is '{TRACK_NO}. {PERFORMER} - {TITLE}.{OUTPUT_FMT}'.\n" + 
                        "Available variables:\n\n" +
                        "{PERFORMER} - PERFORMER as specified in .cue file.\n" +
                        "{TITLE} - Track name as specified in .cue file.\n" +
                        "{OUTPUT_FMT} - Output file format e.g. 'mp3'.\n" +
                        "{TRACK_NO} - Track number as specified in .cue file.\n",
                        type=str, default="{TRACK_NO}. {PERFORMER} - {TITLE}.{OUTPUT_FMT}")

    args = argParser.parse_args()

    if args.version:
        print(f"CUE Splitter version {version}.")
        print(f"Copyright 2023 Locchan. MIT License.")
        print(f"https://opensource.org/license/mit/")
        exit(0)

    check_args(args)

    if os.path.isfile(args.path):
        print("The specified path is a file. Parsing...")
        encode_single_cue(args)
    elif os.path.isdir(args.path):
        print("The specified path is a directory. Walking through...")
        encode_directory(args)

def encode_single_cue(args):
    currcue = CueSheet()
    currcue.setOutputFormat("")
    try:
        with open(args.path, "r", encoding=args.encoding) as cue_file:
            currcue.setData(cue_file.read())
        currcue.parse()
    except Exception as e:
        print("Could not parse .cue file: {} : {}".format(args.path, e.__class__.__name__))
        exit(1)
    encode_cue(os.path.dirname(os.path.realpath(args.path)), currcue, args.output_path, args.output_format, args.output_bitrate, args.additional_ffmpeg_params, args.custom_ffmpeg_path, args.filename_template)

def encode_directory(args):
    cue_files = []
    
    for relpath, dirs, files in os.walk(args.path):
        for afile in files:
            if afile.endswith(".cue"):
                cue_files.append((relpath, afile))

    for acue_file in cue_files:
        print(acue_file)
        cue_path = os.path.join(acue_file[0], acue_file[1])
        output_path = os.path.join(args.output_path, os.path.relpath(acue_file[0], start=args.path))
        try:
            currcue = CueSheet()
            currcue.setOutputFormat("")
            with open(cue_path, "r", encoding=args.encoding) as cue_file:
                currcue.setData(cue_file.read())
            currcue.parse()
        except Exception as e:
            print("Could not parse .cue file: {} : {}".format(cue_path, e.__class__.__name__))
            continue
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        encode_cue(acue_file[0], currcue, output_path, args.output_format, args.output_bitrate, args.additional_ffmpeg_params, args.custom_ffmpeg_path, args.filename_template)

if __name__ == "__main__":
    main()