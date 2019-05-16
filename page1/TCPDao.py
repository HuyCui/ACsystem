from django.http import HttpResponse
from django.http import request
from page1.clientThread import ClientThread
from page1.MsgThread import MsgThread
from page1.Estimate import estimate, estimateDot
from django.core import serializers
import json
from PIL import Image
from page1.Angle import *
import os
from page1 import ScoreDao
from PIL import ImageFile

#路径转换，将windows中存在的 \ 转化为 /
def transform_separator(windows_path):
    linux_path = ''
    if windows_path != '':
        path_list = windows_path.split('\\')
        linux_path = '/'.join(path_list)
    else:
        print("it is null")
    return linux_path


#建立一次tcp连接  返回两张图片的路径以及检测到的flag值
def sendstr():
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    ct = ClientThread('hello')
    ct.start()
    ct.join()
    jpath = {'img': '', 'eimg': ''}
    filepath = 'F:/pycode/Helloweb/Myaction/Myaction/static/'
    abpath = filepath+transform_separator(ct.getimagepath())[18:]
    jpath['img'] = abpath[36:]
    changedpath = abpath.replace('_', '0')
    os.rename(abpath, changedpath)
    im = Image.open(changedpath)
    img_alpha = im.convert('RGBA')
    rot = img_alpha.rotate(-90, expand=1)
    fff = Image.new('RGBA', rot.size, (255, 255, 255, 255))

    out = Image.composite(rot, fff, mask=rot)
    out.convert(im.mode).save(abpath)
    im.close()
    print('**************'+jpath['img'])
    os.remove(changedpath)
    jpath['eimg'], flag = estimate(abpath)

    if flag:  #通过验证 结束线程
        ct.closeconn()
        ct.join()
        ct2 = ClientThread('hello')
        ct2.start()
        ct2.join()
        jpath = {'img': '', 'eimg': ''}
        abpath = 'F:/pycode/Helloweb/Myaction/Myaction/static/' + transform_separator(ct.getimagepath())[18:]
        jpath['img'] = abpath[36:]
        flat = [0.0 for i in range(36)]
        print('**************' + jpath['img'])

        jpath['eimg'], flat = estimateDot(abpath)

    else:  #不通过验证  向树莓派发送信号
        ct.sendsignal()
        ct.closeconn()
        ct.join()

    return json.dumps(jpath), flag

#建立一次tcp连接  返回两张图片的路径以及关键点坐标
def sendstr2():
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    ct = ClientThread('hello')
    ct.start()
    ct.join()
    jpath = {'img': '', 'eimg': ''}
    filepath = 'F:/pycode/Helloweb/Myaction/Myaction/static/'
    abpath = filepath+transform_separator(ct.getimagepath())[18:]
    jpath['img'] = abpath[36:]
    changedpath = abpath.replace('_', '0')
    os.rename(abpath, changedpath)
    im = Image.open(changedpath)
    img_alpha = im.convert('RGBA')
    rot = img_alpha.rotate(-90, expand=1)
    fff = Image.new('RGBA', rot.size, (255, 255, 255, 255))

    out = Image.composite(rot, fff, mask=rot)
    out.convert(im.mode).save(abpath)
    im.close()
    print('**************'+jpath['img'])
    os.remove(changedpath)

    ct.closeconn()
    ct.join()
    ct2 = ClientThread('hello')
    ct2.start()
    ct2.join()
    jpath = {'img': '', 'eimg': ''}
    abpath = 'F:/pycode/Helloweb/Myaction/Myaction/static/' + transform_separator(ct.getimagepath())[18:]
    jpath['img'] = abpath[36:]
    flat = [0.0 for i in range(36)]
    print('**************' + jpath['img'])

    jpath['eimg'], flat = estimateDot(abpath)
    return json.dumps(jpath), flat   #bug
    #return jpath, flat


def sendstr3():

    ct = MsgThread('hello')
    ct.start()
    ct.closeconn()
    ct.join()
    #return jpath, flat

#建立一次tcp连接  返回两张图片的路径以及检测到的flag值
'''
#backup
def sendstr():
    ct = ClientThread('hello')
    ct.start()
    ct.join()
    jpath = {'img': '', 'eimg': ''}
    abpath = 'F:/pycode/Helloweb/Myaction/Myaction/static/'+transform_separator(ct.getimagepath())[18:]
    jpath['img'] = abpath[36:]
    print('**************'+jpath['img'])
    jpath['eimg'], flag = estimate(abpath)
    print(jpath)
    return json.dumps(jpath), flag
'''




#接收ajax请求，每次请求进行验证，如果验证不通过，重新建立tcp连接
def askimage(request):

    while True:
        jpath, flag = sendstr()
        if not flag:
            jpath, flag = sendstr()
        else:
            return HttpResponse(jpath)



#接收ajax请求，每次请求进行验证，如果验证不通过，重新建立tcp连接
def imagescore(request):

    jpath, flat = sendstr2()
    actionid = request.COOKIES.get('actionid')
    print(actionid)
    angles, score = getAngleDic(flat, int(actionid))#返回计算出的角度
    #jpath['score'] = '90'
    temp = json.loads(jpath)
    score *= 10
    temp['score'] = score
    ScoreDao.saveScore(score)

    return HttpResponse(json.dumps(temp))


def stopaction(request):

    sendstr3()
    return HttpResponse('true')




