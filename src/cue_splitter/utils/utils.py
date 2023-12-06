import os
from errno import ENOENT

def construct_name(template, cue_sheet, track, output_format, index):
    return template.format(PERFORMER=track.performer, TITLE=track.title, TRACK_NO=index, OUTPUT_FMT=output_format)

def check_args(args):
    if args.output_path is None:
        if os.path.isfile(args.path):
            args.output_path = os.path.dirname(os.path.realpath(args.path))
        else:
            args.output_path = args.path

    if not os.path.exists(args.path):
        print("Input path does not exist. Cannot proceed...")
        exit(ENOENT)
    
    if args.custom_ffmpeg_path is not None and not os.path.exists(args.custom_ffmpeg_path):
        print("Could not find ffmpeg binary by the path provided.")
        exit(ENOENT)

def construct_metadata(cue_sheet, track, index):
    metadata = {}
    metadata["artist"] = track.performer
    metadata["title"] = track.title
    metadata["album"] = cue_sheet.title
    metadata["track"] = index
    return metadata