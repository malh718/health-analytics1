import pandas as pd 
import numpy as np

pt_age= 18
pt_name='samantha'
pt_char= ['6 foot','black hair','brown eyes'] 

provider_dict= {
    'providerID': [1,2],
    'providersInfo' : [
        {
            'name': 'Dr.Bailey',
            'speciality': 'surgery'
        },
        { 'name': 'Dr. Grey',
           'speciality' :' general medicine'
        }
    ]
}
print ('Patient name is',pt_name)
print ('Patient age  is',pt_age)
print ('Patient characteristics include: ',pt_char)
print ('Show provider_dict:',provider_dict)




def bpChecker(sys, dia):
    if sys >= 120: 
        sys_output= 'not good'
    else: 
        sys_output='its alright' 
    if dia >= 80:
        dia_ouput='not good'
    else:
        dia_ouput='its okay'
    output=[ sys_output,dia_ouput]
    return output

sys_input= 118
dia_input= 81 



bp_result= bpChecker(sys_input, dia_input)
print ('Systolic num: ', sys_input)
print ('Diastolic num: ',dia_input)
print ("blood pressure analysis:", bp_result)

