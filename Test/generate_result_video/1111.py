import xlwt
import numpy as np

book = xlwt.Workbook(encoding='utf-8', style_compression=0)

acti_class = ['Digging', 'Digging', 'Digging',
              'Swing', 'Swing', 'Swing', 'Swing',
              'Loading', 'Loading', 'Loading','Loading', 'Loading', 'Loading', 'Loading', 'Loading',
              'Swing', 'Swing','Swing', 'Swing', 'Swing', 'Swing', 'Swing', 'Swing',
              'Digging', 'Digging','Digging', 'Digging', 'Digging', 'Digging',
              'Swing', 'Swing', 'Swing', 'Swing', 'Swing','Swing', 'Swing', 'Swing', 'Swing',
              'Loading', 'Loading', 'Loading','Loading', 'Loading', 'Loading', 'Loading', 'Loading','Swing','Swing','Swing','Digging', 'Digging', 'Digging', 'Digging']
dict_all = {"Digging": [0, 0], "Loading": [0, 0], "Swing": [0, 0]}



dict_all.setdefault('{}'.format(acti_class[0],[]))[0] = 1
for i in range(len(acti_class)-1):
        if acti_class[i] == acti_class[i + 1]:
            dict_all.setdefault('{}'.format(acti_class[i], []))[1] = dict_all.setdefault('{}'.format(acti_class[i], []))[1] + 1
        else:
            dict_all.setdefault('{}'.format(acti_class[i], []))[1] = dict_all.setdefault('{}'.format(acti_class[i], []))[1] + 1
            dict_all.setdefault('{}'.format(acti_class[i + 1]), [])[0] = dict_all.setdefault('{}'.format(acti_class[i + 1]), [])[0] + 1
        print(dict_all)


dig_count=[0]
filename='./write.txt'

with open(filename, 'w') as f:
    for i in range(len(acti_class) - 1):
        if acti_class[i] != acti_class[i + 1]:
            a=acti_class[i]+str(i+1)
            dig_count.append(a)
            f.write("{} {} \n".format(i + 1, acti_class[i]))
    f.write("{} {} \n".format(len(acti_class)-1, acti_class[len(acti_class)-1]))
    dig_count.append(acti_class[len(acti_class)-1]+str(len(acti_class)-1))
    print(dig_count)


for i in range(0,10,2):
    print(i)

'''cycle_time = []
        for i in range(1,len(dig_count)):
            #    print(dig_count[i][:7])
            if dig_count[i][:7] == 'Digging':
                cycle_time.append(dig_count[i-1][5:])
        print(cycle_time)

for i in range(0, len(clips), unit):
    n_elements = min(unit, len(clips) - i)  # n_elements=unit
    scores = np.array(clips[i]['scores'])  # scores=scores every unit steps
    for j in range(i, min(i + unit, len(clips))):
        scores += np.array(clips[i]['scores'])  # scores self plus for unit times
    scores /= n_elements  # original scores*3/2(unit=2)
    unit_classes.append(class_names[np.argmax(scores)])
    unit_segments.append([clips[i]['segment'][0],
                          clips[i + n_elements - 1]['segment'][1]])
-------------------------------------------------------------------------
 for i in range(1, len(clips), unit):
            scores_1.append(clips[i]['scores'])
        if len(clips)%2 == 0:
            scores_1.append([0,0,0])

        for i in range(0, len(clips), unit):
            n_elements = min(unit, len(clips) - i)
            scores_2 = clips[i]['scores']
            aa=int(i/2)
            print(aa)
            scores = np.array(scores_2) + np.array(scores_1[aa-1])
            scores /= n_elements
            unit_classes.append(class_names[np.argmax(scores)])
            unit_segments.append([clips[i]['segment'][0],
                                  clips[i + n_elements - 1]['segment'][1]])
                                  -----------------------------------------------
                                          cycle_time = {"number of cycles":[],"cycle time":[]}
        file_name='./writecycle'
#write cycle
        c=0
        with open (file_name, 'w') as f:
            for i in range(1, len(dig_count)):
                if dig_count[i][:7] =='Digging':
                    c=c+1
                    f.write("cycle nuimber: {} cycle time: {} \n"\
                            .format(c,0.04*int(dig_count[i-1][5:])))


############################################################################
    for index in range(len(results)):
        video_path = os.path.join(video_root_path, results[index]['video'])
        print(video_path)
        clips = results[index]['clips']
        unit_classes = []
        unit_segments = []
        scores_1=[]
        if temporal_unit == 0:
            unit = len(clips)
        else:
            unit = temporal_unit #unit==class_name_list
        for i in range(1, len(clips), unit):
            scores_1.append(clips[i]['scores'])
        if len(clips)%2 == 0:
            scores_1.append([0,0,0])

        for i in range(0, len(clips), unit):
            n_elements = min(unit, len(clips) - i)
            scores_2 = clips[i]['scores']
            aa=int(i/2)
            print(aa)
            print()
            scores = np.array(scores_2) + np.array(scores_1[aa-1])
            unit_classes.append(class_names[np.argmax(scores)])
            unit_segments.append([clips[i]['segment'][0],
                                  clips[i + n_elements - 1]['segment'][1]])
'''







'''for i in range(len(acti_class)-1):
    if i==0:
        dict_all.setdefault('{}'.format(acti_class[0]), [])[0] = 1
    else:
        if acti_class[i] == acti_class[i + 1]:
            dict_all.setdefault('{}'.format(acti_class[i], []))[1] = dict_all.setdefault('{}'.format(acti_class[i], []))[1] + 1
        else:
            dict_all.setdefault('{}'.format(acti_class[i], []))[1] = dict_all.setdefault('{}'.format(acti_class[i], []))[1] + 1
            dict_all.setdefault('{}'.format(acti_class[i + 1]), [])[0] = dict_all.setdefault('{}'.format(acti_class[i + 1]), [])[0] + 1

        print(i)
        print(dict_all)










      act_duration = []
        for m in range(len(os.listdir('/Users/chen/PycharmProjects/Test/tmp/'))):
            ori_duration = round(m * per_duration,2)
            duration = '%.3f' % ori_duration
            act_duration.append(ori_duration)

        overlay = Image.new("RGBA", (100, 100), color=(0, 0, 0, 63))
        dr1 = ImageDraw.Draw(overlay)
        fnt = ImageFont.load_default()
        dr1.text((5, 5), "some text", font=fnt, fill=(255, 255, 255, 160))

        img1.paste(overlay, (64, 64), overlay)
        img1.show()
        img1.save('test.jpg')
        
        
        
        
       num_cyc = 1
        for n in range(len(acti_class) - 1):
            a = acti_class[n]
            b = acti_class[n + 1]
            if a == b:
                num_cyc = num_cyc
            else:
                num_cyc = 1 + num_cyc
        cyc = int(num_cyc / 3)
#        b = int(total_duration[-1])
        productivity = round((cyc*1.78*3600)/total_duration[-1],2)'''
