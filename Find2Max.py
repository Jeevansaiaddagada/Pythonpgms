from pcinput import getFloat
from pcinput import getInteger
from pcinput import getString
num = getInteger("Enter a number of students (it has to be at least 2): ")
counter = 0
m1 = 0
m2 = 0
n1 = "0"
n2 = "0"
while counter < 2 or num > counter:
    name= getString("Enter a student name: ")
    score= getFloat("Enter a student score: ")
    if score > m1:
        m2 = m1
        n2 = n1
        m1 = score
        n1 = name
    if score > m2 and score < m1:
        m2 = score
        n2 = name
    counter += 1
print("Top two students:{}{}{} score is {:.1f}{}{}{} score is {:.1f}".format("\n",n1,"'s",m1,"\n",n2,"'s",m2))
