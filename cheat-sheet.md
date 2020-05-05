pinout

raspistill -k

raspistill -o Desktop/image.jpg
raspivid -o Desktop/video.h264

raspistill -vf -w 640 -h 480 -o Desktop/myvideo/image-0.jpg

ffmpeg -r 5 -t 4 -i "image-%d.jpg" "animation.mov"

ffmpeg -r 5 -t 7 -i "img-%03d.jpg" "adios.mov"

omxplayer animation.mov 