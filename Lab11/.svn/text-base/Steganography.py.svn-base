import numpy
import copy
import zlib
import base64
import re
from enum import Enum

class Type(Enum):
    Gray = 'Gray'
    Color = 'Color'

class Payload:
    def __init__(self,img=None,compressionLevel=-1,xml=None):
        self.img = img
        self.compressionLevel = compressionLevel
        self.xml = xml
        if self.img is None and self.xml is None:
            raise ValueError
        if self.compressionLevel > 9 or self.compressionLevel < -1:
            raise ValueError
        if self.img is not None and isinstance(self.img,numpy.ndarray) is not True:
            raise TypeError
        if self.xml is not None and isinstance(self.xml,str) is not True:
            raise TypeError
        if self.img is not None and self.xml is None:
            if compressionLevel != -1:
                if len(self.img.shape) != 3:
                    self.xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="Gray" size="'+str(self.img.shape[0])+','+str(self.img.shape[1])+'" compressed="True">\n' + base64.b64encode(zlib.compress(self.image2str(self.img),self.compressionLevel)).decode() + '\n</payload>'
                else:
                    self.xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="Color" size="'+str(self.img.shape[0])+','+str(self.img.shape[1])+'" compressed="True">\n' + base64.b64encode(zlib.compress(self.image2str(self.img),self.compressionLevel)).decode() + '\n</payload>'
            else:
                if len(self.img.shape) != 3:
                    self.xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="Gray" size="'+str(self.img.shape[0])+','+str(self.img.shape[1])+'" compressed="False">\n' + base64.b64encode(self.image2str(self.img)).decode() + '\n</payload>'
                else:
                    self.xml = '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="Color" size="'+str(self.img.shape[0])+','+str(self.img.shape[1])+'" compressed="False">\n' + base64.b64encode(self.image2str(self.img)).decode() + '\n</payload>'
        elif self.img is None and self.xml is not None:
            self.str2image()

    def image2str(self,image):
        r=bytes()
        g=bytes()
        b=bytes()
        if len(image.shape) == 3:
            '''row,column,ch = image.shape
            for i in range(0,row):
                for j in range(0,column):
                    r += bytes([image.item(i,j,0)])
                    g += bytes([image.item(i,j,1)])
                    b += bytes([image.item(i,j,2)])
            return r+g+b'''
            return numpy.append(numpy.append(image[:,:,0].flatten(),image[:,:,1].flatten()),image[:,:,2].flatten())
        else:
            return image.flatten()

    def str2image(self):
        result = re.search(r'<payload type="(\w+)" size="([0-9]+),([0-9]+)" compressed="(\w+)">\n(.+)\n</payload>',self.xml)
        if result:
            row = int(result.groups()[1])
            column = int(result.groups()[2])

            s = result.groups()[4]
            s = base64.b64decode(s)
            if result.groups()[3] == "True":
                s = zlib.decompress(s)
        else:
            raise ValueError
        #print(result.groups()[0],result.groups()[1],result.groups()[2],result.groups()[3])
        l = []
        for i in s:
            l.append(i)
        #print(l)
        if result.groups()[0] == "Gray":
            self.img = numpy.array(l).reshape(row,column)
        else:
            self.img = numpy.asarray([[l[i],l[i+int(len(l)/3)],l[i+int(len(l)/3)*2]] for i in range(0,int(len(l)/3))]).reshape(row,column,3)

class Carrier:

    def __init__(self,img):
        if isinstance(img,numpy.ndarray) is not True:
            raise TypeError
        else:
            self.img = img

    def payloadExists(self):
        byte = ""
        msg = ""
        a = self.img.flatten()
        i = 0
        if len(self.img.shape) != 3:
            for by in a:
                bit = int(by) % 2
                if (len(byte) < 8):
                    byte += str(bit)
                else:
                    if len(byte) == 8 and not msg.__contains__("<?xml"):
                        msg += chr(int(byte,2))
                        byte = ""+ str(bit)
                    elif msg.__contains__("<?xml"):
                            return True
                i += 1
                if i > 100 and not msg.__contains__("<?xml"):
                    #print(msg)
                    return False
        else:
            s = self.img[0:1,:,0] % 2
            s = s.flatten()
            s = s.reshape(int(len(s)/8),8)
            for i in s:
                byte =""
                for j in i:
                    byte += str(j)
                msg += chr(int(byte,2))
            if msg.__contains__("<?xml"):
                return True
            else:
                return False

    def clean(self):

        img = self.img
        img = img & 0xfe
        return img
        '''if len(self.img.shape) == 3:
            row,column,ch = self.img.shape
            img = self.img
            print(img)
            for i in range(0,row):
                for j in range(0,column):
                    if img.item(i,j,0) % 2 == 1:
                        img.itemset((i,j,0),img.item(i,j,0) & 0xfe)
                    if img.item(i,j,1) % 2 == 1:
                        img.itemset((i,j,1),img.item(i,j,1) & 0xfe)
                    if img.item(i,j,2) % 2 == 1:
                        img.itemset((i,j,2),img.item(i,j,2) & 0xfe)
            return img
        else:
            img = list(self.img.flatten())
            for i in range(0,len(img)):
                if img[i] % 2 == 1:
                    img[i] -= 1
            row,column = self.img.shape
            return numpy.array(img).reshape(row,column)'''


    def embedPayload(self,payload,override=False):
        if isinstance(payload,Payload) is False:
            raise TypeError
        payloadexit = self.payloadExists()
        if override is False and payloadexit:
                raise Exception("payload exists")

        if len(payload.xml) * 8 > len(self.img.flatten()):
            raise ValueError
        xml = payload.xml
        b = bytearray()
        b.extend(map(ord, xml))
        a = list(b)
        a = numpy.array(a,dtype=numpy.uint8)
        a= numpy.unpackbits(a)
        cimg = copy.deepcopy(self.img)

        if len(self.img.shape) !=3:
            cimg = cimg.flatten()
            tmp = numpy.zeros(len(cimg),dtype=numpy.uint8)
            tmp[len(a):] += 0xff
            tmp[0:len(a)] += 0xfe
            cimg &= tmp
            cimg += numpy.append(a,numpy.zeros(len(cimg)-len(a),dtype=numpy.uint8))
            cimg = cimg.reshape(self.img.shape)
            return cimg
        else:
            row,column,ch = self.img.shape
            size = row*column

            if len(a) <= size:
                tmp = numpy.zeros(size,dtype=numpy.uint8)
                tmp[len(a):size] += 0xff
                tmp[0:len(a)] += 0xfe
                cimg[:,:,0] &= tmp.reshape(cimg[:,:,0].shape)
                cimg[:,:,0] += numpy.append(a,numpy.zeros(size-len(a),dtype=numpy.uint8)).reshape(cimg[:,:,0].shape)
            elif len(a) <= size * 2:
                cimg[:,:,0] = cimg[:,:,0] & 0xfe
                cimg[:,:,0] += a[0:size].reshape(cimg[:,:,0].shape)  #done filling red channel
                #clearing the filled green channel
                tmp = numpy.zeros(size,dtype=numpy.uint8)
                tmp[len(a)-size:size] += 0xff
                tmp[0:len(a)-size] += 0xfe
                cimg[:,:,1] &= tmp.reshape(cimg[:,:,1].shape)
                cimg[:,:,1] += numpy.append(a[size:],numpy.zeros(2*size-len(a),dtype=numpy.uint8)).reshape(cimg[:,:,1].shape)
            elif len(a) <= size * 3:
                cimg[:,:,0] &= 0xfe
                cimg[:,:,0] += a[0:size].reshape(cimg[:,:,0].shape)  #done filling red channel
                cimg[:,:,1] &= 0xfe
                cimg[:,:,1] += a[size:2*size].reshape(cimg[:,:,1].shape)
                #clearing B channel
                tmp = numpy.zeros(size,dtype=numpy.uint8)
                tmp[len(a)-2*size:size] += 0xff
                tmp[0:len(a)-2*size] += 0xfe
                cimg[:,:,2] &= tmp.reshape(cimg[:,:,2].shape)
                cimg[:,:,2] += numpy.append(a[2*size:],numpy.zeros(3*size-len(a),dtype=numpy.uint8)).reshape(cimg[:,:,2].shape)
            return cimg


    def extractPayload(self):
        if self.payloadExists() is not True:
            raise ValueError
        byte = ""
        msg = ""
        a = self.img.flatten()

        if len(self.img.shape) != 3:
            start = False
            for by in a:
                bit = int(by) % 2
                if (len(byte) < 8):
                    byte += str(bit)
                else:
                    if len(byte) == 8 and not msg.__contains__("</payload>"):
                            msg += chr(int(byte,2))
                            byte = ""+ str(bit)
                    elif msg.__contains__("</payload>"):
                            break
                    if msg.__contains__("<?xml") and not start:
                        msg = '<?xml'
                        start = True
            #msg = msg[:-1]
            if msg == "":
                print('msg is empty')
            #print(msg)
            #if msg[-10:] != "</message>":
            #    raise Exception("Carrier Empty")
            return Payload(xml=msg)
        else:
            r = self.img[:,:,0] % 2
            g = self.img[:,:,1] % 2
            b = self.img[:,:,2] % 2
            r = r.flatten()
            r = r.reshape(int(len(r)/8),8)
            g = g.flatten()
            g = g.reshape(int(len(g)/8),8)
            b = b.flatten()
            b = b.reshape(int(len(b)/8),8)
            start = False
            for i in r:
                byte =""
                for j in i:
                    byte += str(j)
                msg += chr(int(byte,2))
                if msg.__contains__("<?xml") and not start:
                        msg = '<?xml'
                        start = True
            for i in g:
                byte =""
                for j in i:
                    byte += str(j)
                msg += chr(int(byte,2))
            for i in b:
                byte =""
                for j in i:
                    byte += str(j)
                msg += chr(int(byte,2))
            return Payload(xml=msg)

if __name__ == "__main__":
    pass