def time_convertor(t):
    if t//60 ==1 and t%60 ==0:
        print("1 hour")
    elif t//60 ==1 and t%60 ==1:
        print("1 hour, 1 minute")
    elif t//60 ==1 and t%60 >1:
        print("1 hour," + str(t%60) + "minutes")
    elif t//60 >1 and t%60 ==0:
        print(str(t//60) + "hours") 
    elif t//60 >1 and t%60 ==1:
        print(str(t//60) + "hours, 1 minute" )
    elif t//60 >1 and t%60 >1:
        print(str(t//60) + "hours," + str(t%60) + "minutes")
        
#Call function to convert time to hours and minutes 

