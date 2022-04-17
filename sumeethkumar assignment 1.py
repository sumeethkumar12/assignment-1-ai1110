import numpy as np
#given statement,(secx-cosx)*(cscx-sinx)*(tanx+cotx)=1;
try:
    x = float(input('Number in degrees: '))
    if x % 90 == 0:
        print('True')
    else:
        x = np.radians(x)
#take csc x =1/sin x ,  sec x =1/cos x ,cotx=1/tanx

        t1 = 1/np.sin(x) - np.sin(x)
        t2 = 1/np.cos(x) - np.cos(x)
        t3 = 1/np.tan(x) + np.tan(x)
        
        t = t1 * t2 * t3
        if round(t) == 1:
            print('True')
        else:
            print('False')

except ZeroDivisionError:
    print('in the except statement')
# since it is true  given statemet is proved 
