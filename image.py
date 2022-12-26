import imageio
import cv2
import scipy.ndimage
img = "razib.jpg"
def grayscale(rgb):
    return np.dot [...,:3],[0.299,0.587,0.114]
def dodge( front ,back):
    result = front*255/(255-back)
    result [result>255 ] = 255
    result[back == 255]=255
    return result.astype('uint8')
S= imageio.imread(img)
g = grayscale(S)
i = 255-g
b= scipy. ndimage.filters(i,sigma=10)
r = dodge(b,g)
