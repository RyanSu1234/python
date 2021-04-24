"""
str = "00000:00000:00000:00000:00000"

請使用list 分割及重組元素

[99999:00000:00000:00000:00000]  第一圈
[00000:99999:00000:00000:00000]  第二圈
[00000:00000:99999:00000:00000]  第三圈
[00000:00000:00000:99999:00000]  第四圈
[00000:00000:00000:00000:99999]  第五圈

只能用一個list個
"""
old_str="00000:00000:00000:00000:00000"
img_list=old_str.split(':')

img_list[0]="99999"
new_str=':'.join(img_list)
display.show(Image(new_str))

img_list[0]="00000"
img_list[1]="99999"
new_str=':'.join(img_list)
display.show(Image(new_str))

img_list[1]="00000"
img_list[2]="99999"
new_str=':'.join(img_list)
display.show(Image(new_str))

img_list[2]="00000"
img_list[3]="99999"
new_str=':'.join(img_list)
display.show(Image(new_str))

img_list[3]="00000"
img_list[4]="99999"
new_str=':'.join(img_list)
display.show(Image(new_str))

img_list[4]="00000"
img_list[5]="99999"
new_str=':'.join(img_list)
display.show(Image(new_str))


















