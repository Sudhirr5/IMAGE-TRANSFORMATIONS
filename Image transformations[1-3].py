
##i)Image Translation
import cv2
import numpy as np
from matplotlib import pyplot as plt
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
image_url = r"C:\Users\admin\Downloads\gray .jpg"
image = cv2.imread(image_url)
tx = 50 
ty = 30  
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]]) 
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
print("Original Image:")
show_image(image)
print("Translated Image:")
show_image(translated_image)

##ii)Image Scaling

import cv2
import numpy as np
from matplotlib import pyplot as plt
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
image_url = r"C:\Users\admin\Downloads\gray .jpg"
image = cv2.imread(image_url)
scale_x = 1.5  
scale_y = 1.5 
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
print("Original image:")
show_image(image)
print("Scaled Image:")
show_image(scaled_image)

##iii)Image Shearing
import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

image_url = r"C:\Users\admin\Downloads\gray .jpg"
image = cv2.imread(image_url)
shear_factor_x = 0.5  
shear_factor_y = 0.2  
shear_matrix = np.float32([[1, shear_factor_x, 0], [shear_factor_y, 1, 0]])

sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))

print("Original Image:")
show_image(image)
print("Sheared Image:")
show_image(sheared_image)
