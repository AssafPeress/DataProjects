#A
x1= input("input a float number ")
x2= input("input a float number ")
x3= input("input a float number ")
try:
    x1=float(x1)
    x2=float(x2)
    x3=float(x3)
except:
    print ('Error: parameters should be float')
        
def My_Func (x1,x2,x3):
    a=(x1+x2+x3)
    if a == 0:
        print ("Not a number – denominator equals zero")
    else:
        while True:
            try:
                b= ((x1+x2+x3)*(x2+x3)*x3)/a
                return (float(b))
                break
            except ValueError:
                print ('None')

#B
hours = float(input('enter an hour you would like to convert '))
minutes = float(input('enter a minutes you would like to convert '))
if hours <= 0 :
    print ('input error')

def Convert (hours, minutes):
    hours *=3600
    minutes *=60
    print(f'the hours convert to seconds: {hours},\nthe mintues convert to seconds {minutes},\nhours and mintues are {hours+minutes} seconds')