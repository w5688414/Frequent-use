import json
from PIL import Image
import numpy as np
src_path='/home/eric/data/deepdrive/bdd100k/labels/bdd100k_labels_images_val.json'
# src_path='/home/eric/data/deepdrive/bdd100k/labels/bdd100k_labels_images_train.json'
src = json.load(open(src_path))
num_files=len(src)


img = Image.open("/home/eric/data/deepdrive/bdd100k/images/100k/test/cabc30fc-e7726578.jpg")
img_array = np.array(img)
img_array.shape

from xml.dom.minidom import Document
from tqdm import tqdm
import os

def json_to_xml(src,save_path):
    
    imageList=[]
    for i in tqdm(range(num_files)):
        anno=src[i]
        img_name = anno['name']

        doc = Document()
        annotation = doc.createElement('annotation')
        # 根节点插入dom树
        doc.appendChild(annotation)
        folder = doc.createElement("folder")
        folder.appendChild(doc.createTextNode("VOC 2007"))
        annotation.appendChild(folder)

        filename = doc.createElement("filename")
        filename.appendChild(doc.createTextNode(img_name))
        annotation.appendChild(filename)

        sizeimage = doc.createElement("size")
        imagewidth = doc.createElement("width")
        imageheight = doc.createElement("height")
        imagedepth = doc.createElement("depth")

        filepath = os.path.join(im_dir,img_name)
        img = Image.open(filepath)
        img_array = np.array(img)
        height,width,depth =img_array.shape

        imagewidth.appendChild(doc.createTextNode(str(width)))
        imageheight.appendChild(doc.createTextNode(str(height)))
        imagedepth.appendChild(doc.createTextNode(str(depth)))

        sizeimage.appendChild(imagewidth)
        sizeimage.appendChild(imageheight)
        sizeimage.appendChild(imagedepth)

        annotation.appendChild(sizeimage)


        for obj in anno['labels']:
            if 'box2d' not in obj:
                continue
            xy = obj['box2d']
            category = obj['category']
            x1, x2 = min(xy['x1'], xy['x2']), max(xy['x1'], xy['x2'])
            y1, y2 = min(xy['y1'], xy['y2']), max(xy['y1'], xy['y2'])

            object = doc.createElement('object')
            name = doc.createElement('name')
            truncated = doc.createElement('truncated')
            difficult = doc.createElement('difficult')

            name.appendChild(doc.createTextNode(category))
            truncated.appendChild(doc.createTextNode("1"))
            difficult.appendChild(doc.createTextNode("0"))

            object.appendChild(name)
            object.appendChild(truncated)
            object.appendChild(difficult)

            bndbox= doc.createElement("bndbox")
            xmin = doc.createElement("xmin")
            ymin = doc.createElement("ymin")
            xmax = doc.createElement("xmax")
            ymax = doc.createElement("ymax")

            xmin.appendChild(doc.createTextNode(str(x1)))
            ymin.appendChild(doc.createTextNode(str(y1)))
            xmax.appendChild(doc.createTextNode(str(x2)))
            ymax.appendChild(doc.createTextNode(str(y2)))

            bndbox.appendChild(xmin)
            bndbox.appendChild(ymin)
            bndbox.appendChild(xmax)
            bndbox.appendChild(ymax)

            object.appendChild(bndbox)

            annotation.appendChild(object)

        xml_file=img_name.split('.')[0]+".xml"
        output_file_path=os.path.join(save_path,xml_file)
        output_object = open(output_file_path, 'w')
        output_object.write(doc.toprettyxml(indent=' ' * 4))
        output_object.close()

        
        
save_path='/home/eric/data/deepdrive/bdd100k/VOC2007/train'
im_dir='/home/eric/data/deepdrive/bdd100k/images/100k/train/'
# save_path='/home/eric/data/deepdrive/bdd100k/VOC2007/val'
# im_dir='/home/eric/data/deepdrive/bdd100k/images/100k/val/'


# json_to_xml(src,save_path)
    
def output_imagelist(src_json_file,dst):
    imagesList = []
    for i in range(len(src_json_file)):
        anno = src_json_file[i]
        filename = anno['name']
        imagesList.append(filename)
    f1 = open(dst,'w')
    for image in imagesList:
        f1.write(image.split('.')[0]+'\n')
    f1.close()
src_path='/home/eric/data/deepdrive/bdd100k/labels/bdd100k_labels_images_train.json'
src = json.load(open(src_path))
# txt_path="/home/eric/data/deepdrive/bdd100k/val.txt"
txt_path="/home/eric/data/deepdrive/bdd100k/train.txt"
output_imagelist(src,txt_path)