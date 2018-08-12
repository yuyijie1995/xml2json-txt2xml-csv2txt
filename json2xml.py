# txt_to_xml.py
# encoding:utf-8
# 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML
from xml.dom.minidom import Document
import cv2
import os
import json


def generate_xml(name,data,img_size,class_ind):
    doc = Document()

    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)

    title = doc.createElement('folder')
    title_text = doc.createTextNode('BDD')
    title.appendChild(title_text)
    annotation.appendChild(title)

    img_name=name+'.jpg'

    title = doc.createElement('filename')
    title_text = doc.createTextNode(img_name)
    title.appendChild(title_text)
    annotation.appendChild(title)

    source = doc.createElement('source')
    annotation.appendChild(source)

    title = doc.createElement('database')
    title_text = doc.createTextNode('The BDD Database')
    title.appendChild(title_text)
    source.appendChild(title)

    title = doc.createElement('annotation')
    title_text = doc.createTextNode('BDD')
    title.appendChild(title_text)
    source.appendChild(title)

    size = doc.createElement('size')
    annotation.appendChild(size)

    title = doc.createElement('width')
    title_text = doc.createTextNode(str(img_size[1]))
    title.appendChild(title_text)
    size.appendChild(title)

    title = doc.createElement('height')
    title_text = doc.createTextNode(str(img_size[0]))
    title.appendChild(title_text)
    size.appendChild(title)

    title = doc.createElement('depth')
    title_text = doc.createTextNode(str(img_size[2]))
    title.appendChild(title_text)
    size.appendChild(title)

    for object2 in data:
        if object2['category'] in class_ind:
            #for object1 in data['objects']:
                #line=split_line.strip().split()
                #if line[0] in class_ind:
            object = doc.createElement('object')
            annotation.appendChild(object)

            title = doc.createElement('name')
            title_text = doc.createTextNode(object2['category'])
            title.appendChild(title_text)
            object.appendChild(title)

            bndbox = doc.createElement('bndbox')
            object.appendChild(bndbox)
            title = doc.createElement('xmin')
            title_text = doc.createTextNode(str(int(float(object2['box2d']['x1']))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymin')
            title_text = doc.createTextNode(str(int(float(object2['box2d']['y1']))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('xmax')
            title_text = doc.createTextNode(str(int(float(object2['box2d']['x2']))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymax')
            title_text = doc.createTextNode(str(int(float(object2['box2d']['y2']))))
            title.appendChild(title_text)
            bndbox.appendChild(title)

    # 将DOM对象doc写入文件
    f = open('anno1/'+name+'.xml','w')
    f.write(doc.toprettyxml(indent = ''))
    f.close()

if __name__ == '__main__':

    class_ind=('bus','traffic light','traffic sign','person','bike','truck','motor','car','train','rider')
    cur_dir=os.getcwd()
    labels_dir=os.path.join(cur_dir,'anno')
    for parent, dirnames, filenames in os.walk(labels_dir):
        for file_name in filenames:
            full_path=os.path.join(parent, file_name)
            f=open(full_path)
            data=json.load(f)
            print(data)
            #split_lines = f.readlines()
            name= data['name']
            img_name=name+'.jpg'
            img_path=os.path.join(os.getcwd()+'/image/',img_name)
            img_size=cv2.imread(img_path).shape
            print(data['frames'])
            print(type(data['frames']))
            for data1 in data['frames']:
                datas=data1
                datass=datas['objects']
                print(datass)
                print(type(datass))

                generate_xml(name,datass,img_size,class_ind)
print('all txts has converted into xmls')