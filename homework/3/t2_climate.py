"""
Topic:輸入溫度，如果溫度>=40度C,顯示: 太熱,
　　　如果溫度<= 10 顯示:太冷, 其他：舒適:

Show:Please input temperature:"
Input1:40
Output:It's too hot.
"""
def determine_temperature(temperature):
    if temperature >= 40:
        print ('hot')
    elif temperature <= 10:
        print ('cold')
    else:
        print ('worm')