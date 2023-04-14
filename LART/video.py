import os
import sys

# Set the directory path where your videos are stored
arg_folder = sys.argv[1]

# Get a list of all MP4 files in the directory
mp4_files = [f for f in os.listdir(arg_folder) if f.endswith('.mp4')]

# Create an HTML string that contains the video code and thumbnail image for each file
videos_html = ''
for mp4_file in mp4_files:
    video_src = os.path.join(arg_folder, mp4_file)
    video_html = "<video width='100%' class='video-results' data-src='" + video_src + "', type='video/mp4' autoplay muted loop></video><br>\n"
    videos_html += video_html
    
    thumbnail_src = video_src.replace('.mp4', '.jpeg')
    thumbnail_html = f"<img class='thumbnail' width='100%' data-src='{thumbnail_src}'><br>\n"
    videos_html += thumbnail_html

    # also create a thumbnail image
    import cv2
    vidcap = cv2.VideoCapture(video_src)
    success, image = vidcap.read()
    if success:
        # save a low quality image, highly compressed
        cv2.imwrite(video_src.replace('.mp4', '.jpeg'), image, [cv2.IMWRITE_JPEG_QUALITY, 10])     # save frame as JPEG file    

    os.system(f"/Users/jathushan/Downloads/ffmpeg -y -i {video_src} -b:v 500k -crf 36 {video_src.replace('.mp4', '_2.mp4')}")

# Add the videos HTML to the page
print(videos_html)


