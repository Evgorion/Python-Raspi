#!/bin/sh
# The file name. I use the date to make finding files easier.
DateTime="`date +%Y-%m-%d_%H.%M.%S`"
name=cam3-$DateTime
# Where the videos will be saved
BASEpath='/media/pi/boot/video'
RECpath=$BASEpath'/cam3'
COPYpath='/home/pi/google_drive'

openRTSP -D 1 -B 10000000 -b 10000000 -4 -d 60 rtsp://10.0.0.200:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream  >  $RECpath/$name.avi
cp $RECpath/$name.avi $COPYpath
# openRTSP -D 1 -c -B 10000000 -b 10000000 -q -Q -F cam_eight -d 60 rtsp://10.0.0.200:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream  >  $RECpath/record-$name.avi &
# ffmpeg -i rtsp://10.0.0.200:554/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp?real_stream -r 15 -vcodec copy -an -t 60 $RECpath/$name.mp4 </dev/null >/dev/null 2>/tmp/cam02.log &

