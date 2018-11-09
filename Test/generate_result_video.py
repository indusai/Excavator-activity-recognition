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
        unit_segments = []
        if temporal_unit == 0:
            unit = len(clips)
        else:
            unit = temporal_unit
        for i in range(0, len(clips), unit):
            n_elements = min(unit, len(clips) - i)
            scores = np.array(clips[i]['scores'])
            for j in range(i, min(i + unit, len(clips))):
                scores += np.array(clips[i]['scores'])
            scores /= n_elements
            unit_classes.append(class_names[np.argmax(scores)])
            unit_segments.append([clips[i]['segment'][0],
                                  clips[i + n_elements - 1]['segment'][1]])



#        for i in range(len(unit_segments)):
 #           print(unit_segments[i])


#        if os.path.exists('tmp'):
#          subprocess.call('rm -rf tmp', shell=True)
#        subprocess.call('mkdir tmp', shell=True)

#        subprocess.call('ffmpeg -i {} tmp/image_%05d.jpg'.format(video_path), shell=True)
        fps = get_fps(video_path, 'tmp')
        per_duration = round(1/fps,2)
#calculate cycle times
        print(unit_classes)
        print(unit_segments)
        acti_class = []
        for i in range(len(unit_classes)):
            for j in range(unit_segments[i][0], unit_segments[i][1] + 1):
                acti_class.append(unit_classes[i][2:])

        dict_all = {"Digging": [0, 0], "Loading": [0, 0], "Swing": [0, 0]}

        dict_all.setdefault('{}'.format(acti_class[0], []))[0] = 1
        for i in range(len(acti_class) - 1):
            if acti_class[i] == acti_class[i + 1]:
                dict_all.setdefault('{}'.format(acti_class[i], []))[1] = \
                dict_all.setdefault('{}'.format(acti_class[i], []))[1] + 1
            else:
#                print(new_acti_class[i + 1], dict_all.setdefault('{}'.format(new_acti_class[i + 1], [])))
                dict_all.setdefault('{}'.format(acti_class[i], []))[1] = \
                dict_all.setdefault('{}'.format(acti_class[i], []))[1] + 1
                dict_all.setdefault('{}'.format(acti_class[i + 1]), [])[0] = \
                dict_all.setdefault('{}'.format(acti_class[i + 1]), [])[0] + 1


        filename = './writetotxt.txt'
        dig_count=[]
        with open(filename, 'w') as f:
            for i in range(len(acti_class) - 1):
                if acti_class[i] != acti_class[i + 1]:
                    a = acti_class[i] + str(i + 1)
                    dig_count.append(a)
                    f.write("{} {} \n".format(i + 1, acti_class[i]))
            f.write("{} {} \n".format(len(acti_class) - 1, acti_class[len(acti_class) - 1]))
            dig_count.append(acti_class[len(acti_class) - 1] + str(len(acti_class) - 1))
            print(dig_count)


        cycle_time = {"number of cycles":[],"cycle time":[]}
        file_name='./writecycle'
#write cycle
        c=0
        with open (file_name, 'w') as f:
            for i in range(1, len(dig_count)):
                if dig_count[i][:7] =='Digging':
                    c=c+1
                    f.write("cycle nuimber: {} cycle time: {} \n".format(c, dig_count[i-1][5:]))
            cyc = c

       #calculate activity time
        num_loa = 0
        num_swi = 0
        num_dig = 0
        dig_list = []
        swi_list = []
        loa_list = []
        total_duration = []
        for i in range(len(acti_class)):
            total_duration.append(round((i + 1) * per_duration, 2))
            time_dig = round(num_dig * per_duration, 2)
            time_swi = round(num_swi * per_duration, 2)
            time_loa = round(num_loa * per_duration, 2)
            if acti_class[i] == 'Digging':
                num_dig = 1 + num_dig
            else:
                if acti_class[i] == 'Swing':
                    num_swi = 1+num_swi
                else:
                    num_loa = 1 + num_loa
            dig_list.append(time_dig)
            swi_list.append(time_swi)
            loa_list.append(time_loa)

        productivity = round((cyc*60*1.25)/total_duration,2)
        for i in range(len(acti_class)):
                image = Image.open('tmp/image_{:05}.jpg'.format(i+1)).convert('RGBA')
                lab_img = Image.new('RGBA', image.size)
                font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),
                                                       'SourceSansPro-Regular.ttf'), 20)
                d = ImageDraw.Draw(lab_img)
                textsize = d.textsize(acti_class[i], font=font)
                rect_position = [10,10,450,150]
                d.rectangle(rect_position, fill=(0, 0, 0, 130))
                d.text((10, 10), acti_class[i],
                       font=font, fill=(0,255,255))
                d.text((10, 40), 'Digging:' + str(dig_list[i])+'s', font = font, fill=(255,0,255))
                d.line([(140,55),(140+dig_list[i],55)], fill=(255,0,255), width=10)
                d.text((10, 70), 'Swing:' + str(swi_list[i]) + 's', font=font, fill=(255, 0, 255))
                d.line([(140, 85), (140+swi_list[i], 85)], fill=(255, 0, 255), width=10)
                d.text((10, 100), 'Loading:' + str(loa_list[i]) + 's', font=font, fill=(255, 0, 255))
                d.line([(140, 115), (140+loa_list[i], 115)], fill=(255, 0, 255), width=10)
                if i == len(acti_class)-1:
                     d.text((230, 40), 'Total time:' + str(round((total_duration[i]/60),2)) + ' min', font=font, fill=(0,255,255))
                     d.text((230,70), 'Cycle:' + str(cyc), font=font, fill=(0,255,255))
                     d.text((230,100), 'Productivity:' + str(productivity)+' LCY/h', font=font, fill=(0,255,255))

                image.paste(lab_img, (10,10), lab_img)
                image = image.convert("RGB")
                image.save('tmp/image_{:05}_pred.jpg'.format(i+1))


        dst_file_path = os.path.join(dst_directory_path, video_path.split('/')[-1])
        subprocess.call('ffmpeg -y -r {} -i tmp/image_%05d_pred.jpg -b:v 1000k {}'.format(fps, dst_file_path),
                        shell=True)
#        if os.path.exists('tmp'):
#           subprocess.call('rm -rf tmp', shell=True)'''

