datavalid = False

while datavalid == False:
    grade1 = input("Type the grade for the first test :")
    try:
        grade1 = float(grade1)
    except:
        print("Invalid input")
        continue
    if grade1 < 0 or grade1 > 10:
        print("The grade has to be betweeon 0 and 10")
        continue
    else:
        datavalid = True
    
datavalid = False

while datavalid == False:
    grade2 = float(input("Type the grade for the second test :"))
    try:
        grade1 = float(grade1)
    except:
        print("Invalid input")
        continue
    if grade2 <0 or grade2 > 10:
        print("The grade has to be betweeon 0 and 10")
        continue
    else:
        datavalid = True

datavalid = False

while datavalid == False:
    totalclasses = int(input("Type the total number of classes :"))
    try:
        grade1 = int(grade1)
    except:
        print("Invalid input")
        continue
    if totalclasses <=0:
        print("The number of classes have to be more that 0")
        continue
    else:
        datavalid = True

datavalid = False

while datavalid == False:
    absences = int(input("Type the classes absent :"))
    try:
        grade1 = int(grade1)
    except:
        print("Invalid input")
        continue
    if absences <0 or absences > totalclasses:
        print("The number of absences cannot be less than 0 or more than the Total classes")
        continue
    else:
        datavalid = True

avggrade = (grade1+grade2)/2
attendance = (totalclasses-absences) / totalclasses

print("The average grade is :", round(avggrade,2))
print("The attendance rate is:", str(round(attendance*100,2))+'%')

if (avggrade >=6 and attendance >= 0.8):
    print("The student has passed")
elif (avggrade <6 and attendance <0.8):
    print("The student has failed because of a grade less than 6 and an attendance rate lesser than 80%")
elif (attendance>=0.8):
    print("The student failed because of average score less than 6")
else:
    print("The student failed becauseof of attendance rate less than 80%")