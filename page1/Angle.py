# -*- coding:utf-8 -*-
import math
import json
import minimu
import time
#需要计算的关键点坐标index
point = {'rshoulder': [1, 2, 3],
         'lshoulder': [1, 5, 6],
         'relbow': [4, 3, 2],
         'lelbow': [5, 6, 7],
         'rhip': [1, 8, 9],
         'lhip': [1, 11, 12],
         'rknee': [8, 9, 10],
         'lknee': [11, 12, 13]}


def audioRemind(filename):
    song = minimu.load(r'F:/pycode/Helloweb/Myaction/Myaction/static/mp3/'+filename)
    song.play()  # 开始播放
    time.sleep(1.9)
    song.stop()

#计算角度
def getAngle(x1, y1, x2, y2, x3, y3):
    # 计算三条边长
    a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
    c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    # 利用余弦定理计算三个角的角度
    A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
    B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
    C = math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))
    # 输出三个角的角度
    print("There three angles are", round(A, 2), round(B, 2), round(C, 2))
    return round(B, 2)

#返回角度的json
def getAngleDic(list, id):
    angles = {}
    points = ['rshoulder', 'lshoulder', 'relbow', 'lelbow', 'rhip', 'lhip', 'rknee', 'lknee']
    # 判断是否存在关键点
    for i in point:
        flag = True
        for j in range(0, 3):
            if list[2 * point[i][j]] == 0:
                flag = False
        if flag:
            B = getAngle(list[2 * point[i][0]], list[2 * point[i][0] + 1],
                         list[2 * point[i][1]], list[2 * point[i][1] + 1],
                         list[2 * point[i][2]], list[2 * point[i][2] + 1])
            angles[i] = B
        else:
            angles[i] = -1
    count = 0
    score = 0.0
    with open("F:/pycode/Helloweb/Myaction/Myaction/static/angles.json", 'r') as load_f:
        load_dict = json.load(load_f)
        for j in range(0,8):
            if angles[points[j]] != -1:
                count += 1
                score += angles[points[j]]/load_dict[id]['standardAngles'][points[j]]
        score /= count
        #print(load_dict[id]['standardAngles']['rshoulder'])

    if angles[points[1]]/load_dict[id]['standardAngles'][points[1]] < 0.9:
        audioRemind('左臂动作.mp3')
    elif angles[points[0]] / load_dict[id]['standardAngles'][points[0]] < 0.9:
        audioRemind('右臂动作.mp3')
    return angles, score

'''
list = [178, 182, 176, 204, 148, 198, 116, 172, 90, 140, 206, 204, 236, 184, 282, 146, 156, 304, 122, 386, 102, 452,
        200, 304, 222, 382, 240, 448, 172, 174, 186, 176, 162, 178, 194, 180]
rst = getAngleDic(list, 1)
with open("F:/pycode/Helloweb/Myaction/Myaction/static/angles.json", 'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict[0]['standardAngles']['rshoulder'])
print(rst)
'''




