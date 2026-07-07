#for_loop.py
present = 0
absent = 0
overtime = 0
half_day = 0
short_day = 0
for i in range(1,3):
    morning = int(input("Enter Morning Time = "))
    evening = int(input("Enter Evening Time = "))

    if morning <= 8 and evening == 18:
        print("Present")
        present += 1
    elif morning <=8 and evening >=18:
        print("overtime")
        overtime +=1
    elif morning <=8 and evening ==13 or morning <= 13 and evening == 18:
        print("Half Day") 
        half_day +=1
    elif morning >=8 and evening <=13 or morning >=13 and evening <=18:
        print("short Day")
        short_day +=1
    else:
        print("absent") 
        absent += 1
        
print("total present =", present)
print("total absent =", absent)
print("total overtime =", overtime)
print("total half_day =", half_day)
print("total short_day =", short_day)







