import json
from collections import defaultdict

name_box_id = defaultdict(list)
id_name = dict()
f = open("jinnan2_round1_train_20190305/jinnan_round1_train.json", encoding='utf-8')
data = json.load(f)

id2name = {}
for dat in data['images']:
    id2name[dat['id']] = dat['file_name']
# f = open('id2name.txt', 'w')
# f.write(str(id2name))
# f.close()
# print('Done writing "id2name.txt"\n')


for ant in data['annotations']:
    id = ant['image_id']
    name = id2name[id]
    cat = ant['category_id']

    if cat >= 1 and cat <= 11:
        cat = cat - 1
    elif cat >= 13 and cat <= 25:
        cat = cat - 2
    elif cat >= 27 and cat <= 28:
        cat = cat - 3
    elif cat >= 31 and cat <= 44:
        cat = cat - 5
    elif cat >= 46 and cat <= 65:
        cat = cat - 6
    elif cat == 67:
        cat = cat - 7
    elif cat == 70:
        cat = cat - 9
    elif cat >= 72 and cat <= 82:
        cat = cat - 10
    elif cat >= 84 and cat <= 90:
        cat = cat - 11

    name_box_id[name].append([ant['bbox'], cat])

f = open('train_jinnan.txt', 'w')
for key in name_box_id.keys():
    f.write(key)
    box_infos = name_box_id[key]
    for info in box_infos:
        x_min = int(info[0][0])
        y_min = int(info[0][1])
        x_max = x_min + int(info[0][2])
        y_max = y_min + int(info[0][3])

        box_info = " %d,%d,%d,%d,%d" % (
            x_min, y_min, x_max, y_max, int(info[1]))
        f.write(box_info)
    f.write('\n')
f.close()

print('Done writing "train_jinnan.txt"\n')
