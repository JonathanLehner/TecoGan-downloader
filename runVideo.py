import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--video_id', default=2000, type=int, help='starting scene index')
parser.add_argument('--duration', default=120, type=int, help='scene duration')
parser.add_argument('--start_frame', default=0, type=int, help='start frame in video')
parser.add_argument('--video_key', default=0, type=str, help='video key on the website')

args = parser.parse_args()
video_id = args.video_id
duration = args.duration
start_frame = args.start_frame
video_key = args.video_key

import os

os.system("python dataPrepare.py --start_id {0} --duration {1} --start_frame {2} --video_key {3} --disk_path input_videos".format(video_id, duration, start_frame, video_key))

os.system("python main.py --cudaID 0 --output_dir ./results/ --summary_dir ./results/log/ --mode inference --input_dir_LR ./input_videos/scene_{0} --output_pre scene_{0} --num_resblock 16 --checkpoint ./model/TecoGAN --output_ext png".format(video_id))     

os.system("ffmpeg -framerate 30 -pattern_type glob -i 'results/{0}/*.png' -pix_fmt yuv420p {0}.mp4".format(video_id))

# example input 
# python runVideo.py --video_id 2000 --duration 1200 --start_frame 0 --video_key ph5d2ef2b4d780f 
