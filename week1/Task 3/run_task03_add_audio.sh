Trim audio to 1 minute

ffmpeg -i audio.mp3 -t 60 trimmed_audio.mp3

Merge audio with your video

ffmpeg -i output.mp4 -i trimmed_audio.mp3 -c:v copy -c:a aac -shortest final_video.mp4