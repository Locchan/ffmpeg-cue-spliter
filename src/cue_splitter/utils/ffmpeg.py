import datetime
import os
import shlex
import subprocess
from cue_splitter.utils.utils import construct_name
from cue_splitter.utils.utils import construct_metadata

def encode_cue(directory, cue_sheet, output_path, output_format, output_bitrate, additional_params, ffmpeg_path, name_template):
    print(f"{datetime.datetime.now()} Starting encoding: {directory}.")
    if ffmpeg_path is None:
        general_cmd = ["ffmpeg"]
    else:
        general_cmd = [ffmpeg_path]
    general_cmd.append("-i")
    general_cmd.append(os.path.join(directory, cue_sheet.file))
    for index, atrack in enumerate(cue_sheet.tracks, 1):
        cmd = list(general_cmd)
        metadata = construct_metadata(cue_sheet, atrack, index)
        for akey, aval in metadata.items():
            cmd.append("-metadata")
            cmd.append(f"{akey}={aval}")
        cmd.append("-ss")
        cmd.append(convert_offset(atrack.offset))
        if atrack.duration is not None:
            cmd.append("-t")
            cmd.append(str(atrack.duration.total_seconds()))
        cmd.append("-b:a")
        cmd.append(f"{output_bitrate}k")
        if additional_params is not None:
            cmd.extend(shlex.split(additional_params))
        cmd.append(f"{os.path.join(output_path, construct_name(name_template, cue_sheet, atrack, output_format, index))}")
        print(f"\n{cmd}\n")
        subprocess.run(cmd, shell=True, check=True)
    print(f"{datetime.datetime.now()} Finished encoding: {directory}.")

def convert_offset(atime):
    time_split = atime.split(":")
    result = ":".join(time_split[:-1])
    result += f".{time_split[-1]}"
    return result
        