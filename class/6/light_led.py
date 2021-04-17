from microbit import *
boat1 = Image ('90000:'
              '09000:'
              '00900:'
              '00090:'
              '00009')
boat2 = Image ('09000:'
               '00900:'
               '00090:'
               '00009:'
               '90000')
boat3 = Image ('00900:'
               '00090:'
               '00009:'
               '90000:'
               '09000')
boat4 = Image ('00090:'
               '00009:'
               '90000:'
               '09000:'
               '00900')
boat5 = Image ('00009:'
               '90000:'
               '09000:'
               '00900:'
               '00090')
boat = [boat1,boat2,boat3,boat4,boat5]
display.show(boat, delay=1000)

























