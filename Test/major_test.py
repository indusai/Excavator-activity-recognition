import os
import sys
import json
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont


# samp_duration = 10

def get_fps(video_file_path, frames_directory_path):
    p = subprocess.Popen('ffprobe {}'.format(video_file_path),
                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, res = p.communicate()
    res = res.decode('utf-8')

    duration_index = res.find('Duration:')
    duration_str = res[(duration_index + 10):(duration_index + 21)]
    hour = float(duration_str[0:2])
    minute = float(duration_str[3:5])
    sec = float(duration_str[6:10])
    total_sec = hour * 3600 + minute * 60 + sec

    n_frames = len(os.listdir(frames_directory_path))
    fps = round(n_frames / total_sec, 2)
    return fps


if __name__ == '__main__':
    result_json_path = sys.argv[1]
    video_root_path = sys.argv[2]
    dst_directory_path = sys.argv[3]
    if not os.path.exists(dst_directory_path):
        subprocess.call('mkdir -p {}'.format(dst_directory_path), shell=True)
    class_name_path = sys.argv[4]
    temporal_unit = int(sys.argv[5])
    with open(result_json_path, 'r') as f:
        results = json.load(f)

    with open(class_name_path, 'r') as f:
        class_names = []
        for row in f:
            class_names.append(row[:-1])

    for index in range(len(results)):
        video_path = os.path.join(video_root_path, results[index]['video'])
        print(video_path)
        clips = results[index]['clips']
        unit_classes = []
        unit_segments = []
        scores_1 = []
        if temporal_unit == 0:
            unit = len(clips)
        else:
            unit = temporal_unit  # unit==class_name_list
        for i in range(1, len(clips), unit):
            scores_1.append(clips[i]['scores'])
        if len(clips) % 2 == 0:
            scores_1.append([0, 0, 0])

        for i in range(0, len(clips), unit):
            n_elements = min(unit, len(clips) - i)
            scores_2 = clips[i]['scores']
            aa = int(i / 2)
            scores = np.array(scores_2) + np.array(scores_1[aa - 1])
            unit_classes.append(class_names[np.argmax(scores)])
            unit_segments.append([clips[i]['segment'][0],
                                  clips[i + n_elements - 1]['segment'][1]])

    print(unit_segments)
    new_segments = []
    for i in range(0, len(unit_classes),3):
        major = 0
        count = 0
        for j in range(i, min(i+3, len(unit_classes))):
            if count == 0:
                major = unit_classes[j]
                count = count+1
            elif major == unit_classes[j]:
                count = count+1
            else:
                count = count-1
 #           print(unit_classes[j])
#        print("----------")
#        print(major)
 #       print("////////////")
        new_segments.append([clips[i]['segment'][0], clips[i+6-1]['segment'][1]])
    print(new_segments)

#unit_segments.append([clips[i]['segment'][0],
#                                  clips[i + n_elements - 1]['segment'][1]])







