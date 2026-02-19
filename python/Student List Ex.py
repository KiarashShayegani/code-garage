# Python intermediate training

students=[
    {'Name' : 'Jack',
     'Student Number': 124,
     'courses':[
         {'Lesson' : 'Lab 1','units':3, 'Mark':17},
         {'Lesson' : 'Electronics','units':2, 'Mark':15}
        ] 
    },
    
    {'Name' : 'Sam',
     'Student Number': 563, 
     'courses':[
         {'Lesson' : 'Lab 1','units':3, 'Mark':19},
         {'Lesson' : 'Litrature','units':1, 'Mark':18},
         {'Lesson' : 'PCB','units':1, 'Mark':12}
         ]
    },

    {'Name' : 'Abigail',
     'Student Number': 782, 
     'courses':[
         {'Lesson' : 'Lab 1','units':3, 'Mark':14},
         {'Lesson' : 'French Language','units':2, 'Mark':17}
         ]
    }
]

studentNum = int(input('Enter student ID to receive info: '))

while studentNum != -1:
    for s in students:
        if studentNum == int(s['Student Number']):
            print('Student Name : ' + s['Name'])
            print('Student ID : ' + str(s['Student Number']))
            for c in s['courses']:
                print('Lesson ' + c['Lesson'] + ' with ' + str(c['units']) + ' units, mark is: ' + str(c['Mark']))
            studentNum = int(input('Enter student ID again(-1 to exit): '))
        #else:
    print('Student was not found!')
    studentNum = int(input('Enter student ID again(-1 to exit): '))


# while studentNum != -1:
#     for s in students:
#         if studentNum == int(s['Student Number']):
#             print('Student Name : ' + s['Name'])
#             print('Student ID : ' + str(s['Student Number']))
#             for c in s['courses']:
#                 print('Lesson ' + c['Lesson'] + ' with ' + str(c['units']) + ' units, mark is: ' + str(c['Mark']))
#             studentNum = int(input('Enter student ID again(-1 to exit): '))

#         else:
#             print('Student was not found!')
#             studentNum = int(input('Enter student ID again(-1 to exit): '))


#print('student was not found!')
#studentNum = int(input('Enter student ID again(-1 to exit): '))