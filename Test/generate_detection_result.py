import os
import sys
import json
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont


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

        if temporal_unit == 0:
            unit = len(clips)
        else:
            unit = temporal_unit
        for i in range(0, len(clips), unit):
            n_elements = min(unit, len(clips) - i)
            scores = np.array(clips[i]['scores'])
            for j in range(i, min(i + unit, len(clips))):
                scores = np.array(clips[i]['scores'])
            unit_classes.append(class_names[np.argmax(scores)])


        new_segments = []
        major_list = []
        for i in range(0, len(unit_classes), 4):
            elements = min(4, len(unit_classes) - i)
            major = 0
            count = 0
            for j in range(i, min(i + 4, len(unit_classes))):
                if count == 0:
                    major = unit_classes[j]
                    count = count + 1
                elif major == unit_classes[j]:
                    count = count + 1
                else:
                    count = count - 1
            major_list.append(major)
            new_segments.append([clips[i]['segment'][0], clips[i+elements-1]['segment'][1]])
        print(new_segments)
        print(major_list)

        new_acti_class = []
        for i in range(len(major_list)):
            for j in range(new_segments[i][0], new_segments[i][1]+1):
                new_acti_class.append(major_list[i][2:])



#        if os.path.exists('tmp'):
#          subprocess.call('rm -rf tmp', shell=True)
#        subprocess.call('mkdir tmp', shell=True)

        subprocess.call('ffmpeg -i {} tmp/image_%05d.jpg'.format(video_path), shell=True)
        fps = get_fps(video_path, 'tmp')
        per_duration = round(1/fps,2)
        print(fps)
#calculate cycle times


        dict_all = {"Digging": [0, 0], "Loading": [0, 0], "Swing": [0, 0]}

        dict_all.setdefault('{}'.format(new_acti_class[0], []))[0] = 1
        for i in range(len(new_acti_class) - 1):
            if new_acti_class[i] == new_acti_class[i + 1]:
                dict_all.setdefault('{}'.format(new_acti_class[i], []))[1] = \
                dict_all.setdefault('{}'.format(new_acti_class[i], []))[1] + 1
            else:
#                print(acti_class[i + 1], dict_all.setdefault('{}'.format(acti_class[i + 1], [])))
                dict_all.setdefault('{}'.format(new_acti_class[i], []))[1] = \
                dict_all.setdefault('{}'.format(new_acti_class[i], []))[1] + 1
                dict_all.setdefault('{}'.format(new_acti_class[i + 1]), [])[0] = \
                dict_all.setdefault('{}'.format(new_acti_class[i + 1]), [])[0] + 1

        filename = './writetotxt.txt'
        dig_count=[]
        with open(filename, 'w') as f:
            for i in range(len(new_acti_class) - 1):
                if new_acti_class[i] != new_acti_class[i + 1]:
                    a = new_acti_class[i] + str(i + 1)
                    dig_count.append(a)
                    f.write("{} {} \n".format(i + 1, new_acti_class[i]))
            f.write("{} {} \n".format(len(new_acti_class) - 1, new_acti_class[len(new_acti_class) - 1]))
            dig_count.append(new_acti_class[len(new_acti_class)-1] + str(len(new_acti_class)))
            print(dig_count)


        file_name='./writecycle'
        c=0
        cycle_time =[0]
        with open (file_name, 'w') as f:
            for i in range(1, len(dig_count)):
                if dig_count[i][:7] =='Digging':
                    c=c+1
                    cycle_time.append(dig_count[i-1][5:])
                    _dur = int(cycle_time[c])-int(cycle_time[c-1])
                    f.write("cycle number: {} cycle time: {} \n".format(c, str(_dur*0.04)))
            cyc = c
        print(cycle_time)
       #calculate activity time
        num_loa = 0
        num_swi = 0
        num_dig = 0
        dig_list = []
        swi_list = []
        loa_list = []
        total_duration = []
        for i in range(len(new_acti_class)):
            total_duration.append(round((i + 1) * per_duration, 2))
            time_dig = round(num_dig * per_duration, 2)
            time_swi = round(num_swi * per_duration, 2)
            time_loa = round(num_loa * per_duration, 2)
            if new_acti_class[i] == 'Digging':
                num_dig = 1 + num_dig
            else:
                if new_acti_class[i] == 'Swing':
                    num_swi = 1+num_swi
                else:
                    num_loa = 1 + num_loa
            dig_list.append(time_dig)
            swi_list.append(time_swi)
            loa_list.append(time_loa)

        productivity = round((cyc * 60 * 1.74) / 1.1, 2)
        for i in range(len(new_acti_class)):
            image = Image.open('tmp/image_{:05}.jpg'.format(i + 1)).convert('RGBA')
            lab_img = Image.new('RGBA', image.size)
            font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),
                                                   'SourceSansPro-Regular.ttf'), 25)
            d = ImageDraw.Draw(lab_img)
            textsize = d.textsize(new_acti_class[i], font=font)
#            rect_position = [10, 10, 450, 150]
#            d.rectangle(rect_position, fill=(0, 0, 0, 150))
            d.text((10, 10), new_acti_class[i],
                   font=font, fill=(0, 255, 255))
            d.text((10, 40), 'Digging:' + str(dig_list[i]) + 's', font=font, fill=(255, 0, 255))
            d.line([(150, 60), (150 + dig_list[i], 60)], fill=(255, 0, 255), width=10)
            d.text((10, 70), 'Swing:' + str(swi_list[i]) + 's', font=font, fill=(255, 0, 255))
            d.line([(150, 90), (150 + swi_list[i], 90)], fill=(255, 0, 255), width=10)
            d.text((10, 100), 'Loading:' + str(loa_list[i]) + 's', font=font, fill=(255, 0, 255))
            d.line([(150, 120), (150 + loa_list[i], 120)], fill=(255, 0, 255), width=10)
            if i == len(new_acti_class) - 1:
                d.text((250, 40), 'Total time:' + str(total_duration[-1]) + 's', font=font,
                       fill=(0, 255, 255))
                d.text((250,70), 'Cycle:' + str(cyc), font=font, fill=(0,255,255))
                d.text((250,100), 'Productivity:' + str(productivity)+' LCY/h', font=font, fill=(0,255,255))

            image.paste(lab_img, (10, 10), lab_img)
            image = image.convert("RGB")
            image.save('tmp/image_{:05}_pred.jpg'.format(i + 1))

        dst_file_path = os.path.join(dst_directory_path, video_path.split('/')[-1])
        subprocess.call('ffmpeg -y -r {} -i tmp/image_%05d_pred.jpg -b:v 1000k {}'.format(fps, dst_file_path),
                        shell=True)

#        if os.path.exists('tmp'):
#           subprocess.call('rm -rf tmp', shell=True)'''

