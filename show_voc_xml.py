import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image,ImageFont,ImageDraw,ImageFont

classes = ['helmet']
# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


def convert_annotation(image_id):
    
    im_path  = ('JPEGImages/%s.jpg'%(image_id))
    im = Image.open(im_path)
    xml_path = open('Annotations/%s.xml'%(image_id))
    tree=ET.parse(xml_path)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    draw = ImageDraw.Draw(im)
    # print(w,h)
    for obj in root.iter('object'):
        difficult = 0
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        x1,x2,y1,y2 = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        # if int(difficult)==0:
        draw.rectangle([x1,y1,x2,y2], outline='red', fill=None)

        # 防止越界
        if y1-15>=10:
            draw.text([x1,y1-15],classes[cls_id],"black")
        else:
            draw.text([x1,y1],classes[cls_id],"black")

    im.show()
    # im.save('voc2007_with_person/'+image_id+'.jpg')


if __name__ == '__main__':
    convert_annotation('0a6291ad-323f-341d-88f5-f7c7066752c0')


    # bad:2010_006507,2010_006104,2010_006097,2010_006158,
    # many persons:2010_004439,2010_004597,
    # small objects
    # difficult