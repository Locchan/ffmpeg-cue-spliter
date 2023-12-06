CUE Splitter
=========

Simple CUE splitter written in python.

Depends on `CueParser <https://github.com/artur-shaik/CueParser>`_ (MIT License).


Usage
=========
  -v, --version         Display version and license info.
  -p PATH, --path PATH  Path to the .cue file or directory with .cue file(s).
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        Output path. Default is the path from --path.
  -b OUTPUT_BITRATE, --output-bitrate OUTPUT_BITRATE
                        Bitrate of the output (kbps). Default is 320kbps.
  -f OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                        Output format. Default is mp3.
  -a ADDITIONAL_FFMPEG_PARAMS, --additional-ffmpeg-params ADDITIONAL_FFMPEG_PARAMS
                        Additional parameters to pass to ffmpeg while encoding. Default: '-nostdin'
  -e ENCODING, --encoding ENCODING
                        .cue file encoding. Default is utf-8.
  -c CUSTOM_FFMPEG_PATH, --custom-ffmpeg-path CUSTOM_FFMPEG_PATH
                        Custom path for ffmpeg executable.
  -t FILENAME_TEMPLATE, --filename-template FILENAME_TEMPLATE
                        Template for resulting filenames. Default is '{TRACK_NO}. {PERFORMER} - {TITLE}.{OUTPUT_FMT}'.

Available variables for FILENAME_TEMPLATE:

  {PERFORMER} - Performer as specified in .cue file.
  
  {TITLE} - Track name as specified in .cue file.
  
  {OUTPUT_FMT} - Output file format e.g. 'mp3'.
  
  {TRACK_NO} - Track number as specified in .cue file.
