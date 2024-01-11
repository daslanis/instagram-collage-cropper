from PIL import Image 
import os

# Change string below to the path of the image you would like to crop
im = Image.open("input.png") 

width, height = im.size 

def FixSquare(width = width, height = height):
  if width == height:
    if width / 3 == int(width / 3):
      return (width)

    elif ((width - 1 )/ 3) == int((width - 1)/ 3):
      return (width - 1)

    elif ((width - 2 )/ 3) == int((width - 2)/ 3):
      return (width - 2)

width = FixSquare()

#==============
left = [0 , width/3 , (width/3)*2 , 0 , width/3 , (width/3)*2 , 0 , width/3 , (width/3)*2]
top = [0 ,0 ,0 , width/3 , width/3 , width/3 , (width/3)*2 ,  (width/3)*2 , (width/3)*2]
right = [ width/3, (width/3)*2 , width, width/3, (width/3)*2 , width, width/3, (width/3)*2 , width]
bottom = [ width/3, width/3, width/3, (width/3)*2 , (width/3)*2 , (width/3)*2 ,width, width, width]
#==============

if not os.path.exists("cropped_images"):
    os.makedirs("cropped_images")

repeat = 0
while repeat < 9:
  left1 = left[repeat]
  top1 = top[repeat]
  right1 = right[repeat]
  bottom1 = bottom[repeat]

  im1 = im.crop((left1, top1, right1, bottom1))
  im1.save(str('cropped_images/' + str(repeat + 1) + '.png'))
  repeat = repeat + 1
