marks=[]
for x in range(5):
    marks.append(int(input("Enter marks: ")))
#print(max(marks))
marks.sort()
print(f"Highest obtained mark is {marks[-1]}")
sum=0
for i in range(len(marks)):
    sum+=marks[i]
print(f"Average marks:{sum/len(marks)}")
print(f"Percentage of marks:{(sum/len(marks)/10)*100}")