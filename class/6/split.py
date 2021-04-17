from microbit import *

old_str="09090:09090:09090:99999:09990"
img_list=old_str.split(':')
length=len(img_list)

img_list[0]="99999"
new_str=':'.join(img_list)

display.show(Image(new_str))
























