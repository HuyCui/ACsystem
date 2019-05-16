import argparse
import logging
import sys
import time
import json
import minimu
sys.path.append("F:\\pycode\\tf-pose-estimation-master")

from tf_pose import common
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from PIL import Image

def estimate(path):
    logger = logging.getLogger('TfPoseEstimatorRun')
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    '''
    parser = argparse.ArgumentParser(description='tf-pose-estimation run')
    parser.add_argument('--image', type=str, default=path)
    parser.add_argument('--model', type=str, default='mobilenet_thin',
                        help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. '
                             'default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    args = parser.parse_args()
    '''
    w, h = model_wh('0x0')
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(w, h))

    # estimate human poses from a single image !
    image = common.read_imgfile(path, None, None)
    if image is None:
        logger.error('Image can not be read, path=%s' % path)
        sys.exit(-1)

    t = time.time()
    humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
    # print(json.dumps(dict(humans)))
    # print(humans[0])
    elapsed = time.time() - t

    logger.info('inference image: %s in %.4f seconds.' % (path, elapsed))
    flat = [0.0 for i in range(36)]
    image, flat = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
    # print(flat)
    flag = False
    if flat[28] + flat[29] == 0:
        song = minimu.load(r'F:/pycode/Helloweb/Myaction/Myaction/static/mp3/正在校正.mp3')
        song.play()  # 开始播放
        time.sleep(1.2)
        song.stop()
        flag = False
        print('the camera should be risen up')
    else:
        song = minimu.load(r'F:/pycode/Helloweb/Myaction/Myaction/static/mp3/校正完成.mp3')
        song.play()  # 开始播放
        time.sleep(1.2)
        song.stop()
        flag = True
    # 将numpy数组保存为图片
    bgimg = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_BGR2RGB)
    Image.fromarray(bgimg).save('F:/pycode/Helloweb/Myaction/Myaction/static/img/frompi/'+'new_'+path[-13:-4]+'.jpg')
    return '/static/img/frompi/'+'new_'+path[-13:-4]+'.jpg', flag

#返回数组和路径
def estimateDot(path):
    logger = logging.getLogger('TfPoseEstimatorRun')
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


    w, h = model_wh('0x0')
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(w, h))

    # estimate human poses from a single image !
    image = common.read_imgfile(path, None, None)
    if image is None:
        logger.error('Image can not be read, path=%s' % path)
        sys.exit(-1)

    t = time.time()
    humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
    # print(json.dumps(dict(humans)))
    # print(humans[0])
    elapsed = time.time() - t

    logger.info('inference image: %s in %.4f seconds.' % (path, elapsed))
    flat = [0.0 for i in range(36)]
    image, flat = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
    # print(flat)


    # 将numpy数组保存为图片
    bgimg = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_BGR2RGB)
    Image.fromarray(bgimg).save('F:/pycode/Helloweb/Myaction/Myaction/static/img/frompi/'+'new_'+path[-13:-4]+'.jpg')
    return '/static/img/frompi/'+'new_'+path[-13:-4]+'.jpg', flat


#estimate('F:/pycode/Helloweb/Myaction/Myaction/static/img/frompi/new_image.jpg')