# IMAGE-TRANSFORMATIONS


## Aim
To perform image transformation such as Translation, Scaling, Shearing, Reflection, Rotation and Cropping using OpenCV and Python.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import the necessary libraries and read the original image and save it as a image variable.

### Step2:
Translate the image using a function warpPerpective()

### Step3:
Scale the image by multiplying the rows and columns with a float value.

### Step4:
Shear the image in both the rows and columns.

### Step5:
Find the reflection of the image.

### Step 6:
Rotate the image using angle function.

## Program:
```
Developed By: SUDHIR KUMAR. R
Register Number: 212223230221
```

### i)Image Translation

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display images in Colab
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Load an image from URL or file path
image_url = r"C:\Users\admin\dig-img-process\fie.jpg"
image = cv2.imread(image_url)

# Define translation matrix
tx = 50  # Translation along x-axis
ty = 30  # Translation along y-axis
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])  # Create translation matrix

# Apply translation to the image
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Display original and translated images
print("Original Image:")
show_image(image)
print("Translated Image:")
show_image(translated_image)
```

### ii) Image Scaling

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display images in Colab
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Load an image from URL or file path
image_url = r"C:\Users\admin\dig-img-process\fie.jpg"
image = cv2.imread(image_url)

# Define scale factors
scale_x = 1.5  # Scaling factor along x-axis
scale_y = 1.5  # Scaling factor along y-axis

# Apply scaling to the image
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

# Display original and scaled images
print("Original image:")
show_image(image)
print("Scaled Image:")
show_image(scaled_image)
```

### iii)Image shearing

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display images in Colab
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Load an image from URL or file path
image_url = r"C:\Users\admin\dig-img-process\fie.jpg"
image = cv2.imread(image_url)

# Define shear parameters
shear_factor_x = 0.5  # Shear factor along x-axis
shear_factor_y = 0.2  # Shear factor along y-axis

# Define shear matrix
shear_matrix = np.float32([[1, shear_factor_x, 0], [shear_factor_y, 1, 0]])

# Apply shear to the image
sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))

# Display original and sheared images
print("Original Image:")
show_image(image)
print("Sheared Image:")
show_image(sheared_image)
```

### iv)Image Reflection

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display images in Colab
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Load an image from URL or file path
image_url = r"C:\Users\admin\dig-img-process\fie.jpg"
image = cv2.imread(image_url)

# Reflect the image horizontally
reflected_image_horizontal = cv2.flip(image, 1)

# Reflect the image vertically
reflected_image_vertical = cv2.flip(image, 0)

# Reflect the image both horizontally and vertically
reflected_image_both = cv2.flip(image, -1)

# Display original and reflected images
print("Original Image:")
show_image(image)
print("Reflected Horizontally:")
show_image(reflected_image_horizontal)
print("Reflected Vertically:")
show_image(reflected_image_vertical)
print("Reflected Both:")
show_image(reflected_image_both)

```

### v)Image Rotation

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display images in Colab
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Load an image from URL or file path
image_url = r"C:\Users\admin\dig-img-process\fie.jpg"
image = cv2.imread(image_url)

# Define rotation angle in degrees
angle = 45

# Get image height and width
height, width = image.shape[:2]

# Calculate rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

# Perform image rotation
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display original and rotated images
print("Original Image:")
show_image(image)
print("Rotated Image:")
show_image(rotated_image)
```

### vi)Image Cropping

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to display images in Colab
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Load an image from URL or file path
image_url = r"C:\Users\admin\dig-img-process\fie.jpg"
image = cv2.imread(image_url)

# Define cropping coordinates (x, y, width, height)
x = 100  # Starting x-coordinate
y = 50   # Starting y-coordinate
width = 200  # Width of the cropped region
height = 150  # Height of the cropped region

# Perform image cropping
cropped_image = image[y:y+height, x:x+width]

# Display original and cropped images
print("Original Image:")
show_image(image)
print("Cropped Image:")
show_image(cropped_image)
```
## Output:

### i)Image Translation

Original Image:
![Screenshot 2024-09-30 153841](https://github.com/user-attachments/assets/f05819e4-c593-4c3d-bf88-d150c4024fc0)

Translated Image:
![Screenshot 2024-09-30 153917](https://github.com/user-attachments/assets/1862ee6f-7246-4611-9716-c80d1deee156)

### ii) Image Scaling

Original Image:
![Screenshot 2024-09-30 154132](https://github.com/user-attachments/assets/66763a4a-1f14-4dd4-9c2a-b353de9d64db)

Scaled Image:
![Screenshot 2024-09-30 154144](https://github.com/user-attachments/assets/269efef2-185e-4e9c-9fda-b3c995801fd1)

### iii)Image shearing

Original Image:
![Screenshot 2024-09-30 154320](https://github.com/user-attachments/assets/dc710403-abd9-414e-bc68-9ad6ee7a4df3)

Sheared Image:
![Screenshot 2024-09-30 154329](https://github.com/user-attachments/assets/0ac707b3-95e1-42d1-bdde-607031540521)

### iv)Image Reflection

Original Image:
![Screenshot 2024-09-30 154534](https://github.com/user-attachments/assets/0df1b35a-bdb0-4f64-ac8e-d60e3838a9dc)

Reflected Horizontally:
![Screenshot 2024-09-30 154548](https://github.com/user-attachments/assets/56876e5a-c716-479e-a67a-e617d7b77e47)

Reflected Vertically:
![Screenshot 2024-09-30 154557](https://github.com/user-attachments/assets/8e6c6b4e-e9a6-4bd8-a8e7-e25aec265943)

Reflected Both Horizontally and Vertically:
![Screenshot 2024-09-30 154606](https://github.com/user-attachments/assets/1676c217-94a1-431f-a5c9-cf7b5d145d9b)

### v)Image Rotation

Original Image:
![Screenshot 2024-09-30 155044](https://github.com/user-attachments/assets/341d7a5d-2cfa-47d8-bffc-2d442c92e39f)

Rotated Image:
![Screenshot 2024-09-30 155058](https://github.com/user-attachments/assets/247cb164-6dbc-4f78-858d-a3cb090e38bf)

### vi)Image Cropping

Original Image:
![Screenshot 2024-09-30 155300](https://github.com/user-attachments/assets/867dcf16-d29d-4ac2-ace2-7ee484d361a8)

Cropped Image:
![Screenshot 2024-09-30 155309](https://github.com/user-attachments/assets/11bb7b97-d879-40e3-a235-7630ef53ddbe)

## Result: 

Thus the different image transformations such as Translation, Scaling, Shearing, Reflection, Rotation and Cropping are done using OpenCV and python programming.
