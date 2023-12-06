CUE Splitter
=========

Simple CUE splitter written in python.

Depends on `CueParser <https://github.com/artur-shaik/CueParser>`_ (MIT License).

Splits lossless .cue + (flac/ape/...) into separate files to any format (mp3/aac/...) that is recognized by your ffmpeg installation.

Retains directory structure if you set a directory as a path to start. Will create the same directory structure in the output path. (Will not do so if the directory does not contain any .cue files).

Cross-platform by design. All you need is ffmpeg installed on your system.

Usage
=========
-v, --version  Display version and license info.
-p, --path  Path to the .cue file or directory with .cue file(s).
-o, --output-path  Output path. Default is the path from --path.
-b, --output-bitrate  Bitrate of the output (kbps). Default is 320kbps.
-f, --output-format  Output format. Default is mp3.
-a, --additional-ffmpeg-params  Additional parameters to pass to ffmpeg while encoding. Default: '-nostdin'
-e, --encoding  .cue file encoding. Default is utf-8.
-c, --custom-ffmpeg-path  Custom path for ffmpeg executable.
-t, --filename-template  Template for resulting filenames. Default is '{TRACK_NO}. {PERFORMER} - {TITLE}.{OUTPUT_FMT}'.

Available variables for FILENAME_TEMPLATE:

  {PERFORMER} - Performer as specified in .cue file.
  
  {TITLE} - Track name as specified in .cue file.
  
  {OUTPUT_FMT} - Output file format e.g. 'mp3'.
  
  {TRACK_NO} - Track number as specified in .cue file.
