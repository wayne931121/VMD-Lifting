```cmd
rem create video
ffmpeg -start_number 50001 -framerate 30 -i %5d.png -crf 1 -pix_fmt yuva420p o.mp4

rem smooth video 4 times
ffmpeg -i o.mp4 -filter:v "select=mod(n\,2)" -c:v h264 -c:a copy ben1.mp4
ffmpeg -i ben1.mp4 -filter:v "select=mod(n\,2)" -c:v h264 -c:a copy ben2.mp4
ffmpeg -i ben2.mp4 -filter:v "select=mod(n\,2)" -c:v h264 -c:a copy ben3.mp4
ffmpeg -i ben3.mp4 -filter:v "select=mod(n\,2)" -c:v h264 -c:a copy ben4.mp4
ffmpeg -i ben4.mp4 -filter:v "select=mod(n\,2)" -c:v h264 -c:a copy ben5.mp4

rem slowly video
ffmpeg -i ben7.mp4 -filter:v "setpts=PTS/0.5" -c:v h264 -c:a copy o2.mp4
```
