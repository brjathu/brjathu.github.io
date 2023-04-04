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

# Add the videos HTML to the page
print(videos_html)






#  <div>
#           <div class='row'>
#             <div class='col'>
#               <p class='h2'>More Video Results on Kinetics</p>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_Z2t-F5cubpk_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_--yCUKj4Oq4_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_0YqLJjXmU0I_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_OyO-B-omyS0_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_VoYauMky8IQ_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_6KG0mbhejCs_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_7jv141dj_zM_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_ls1fXwwHW3E_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_-gn_eC6qOk0_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_5YkINInb29k_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_v3huVwrvWE4_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_9_GQ2Sz20ds_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_-HutuMqTAPw_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_xpFW8m5PZCA_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_xtSBE8LFhXY_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_-Y-fUYGcb7o_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val__kcVbo4E2JQ_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_-53DvfE42gE_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_4pJ_UNWqLWQ_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_H9XWa152whU_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_ZCITJQfuVCY_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_OK2iI2F7KIY_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_ySvt7w8irBY_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_lBg84JYUZHM_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_B8WQ7foXaJ4_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_5PvvLJAHj-E_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_61oPN1ONIk8_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_sa2rr6ZQiPE_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val__oQdPnAcCNs_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val__3l3WdE36TI_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_DxCF_5q1ReU_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_-6ykAmBXIr0_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val__AnTe0ywuw0_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <!-- <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_--wYHtYMK9o_.mp4', type='video/mp4' autoplay muted loop></video><br> -->
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_2KQ1mvI_k2Y_.mp4', type='video/mp4' autoplay muted loop></video><br>
#               <video width='100%' class='video-results' src='files/videos_kinetics/kinetics-val_Ls5n1KFnpeU_.mp4', type='video/mp4' autoplay muted loop></video><br>
#             </div>
#           </div>
#         </div>
