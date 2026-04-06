-->Command to extract ~1800 images (30 fps for 1 minute)

ffmpeg -ss 00:00:00 -t 60 -i video.mp4 -vf fps=30 frames_%04d.jpg

Convert images back to video

ffmpeg -framerate 30 -i frames_%04d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4