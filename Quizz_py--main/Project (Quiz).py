import csv
field=[]
ans='y'
while  ans=='y':
    stud=[]
    name=input("Enter your name :")
    admno=int(input("Enter your Admn No :"))
    classes=int(input("Enter your class :"))
    score =0
    question1  =input("Question 1 :- The members of the Rajya Sabha are elected by ? \n a. The people\n b. Lok Sabha \n c. Elected members of the legislative assembly\n d. Elected members of the legislative coucil\n Answer :-")
    if question1=="c"  or question1=="elected member of the legislative assembly":
      score=score+1
      print ("Correct")
      print("Score is",score,"out of 1")
      print("")

    else:
           print("Incorrect","Answer is c, Elected member of legislative assembly")
           print("Score is ",score,"out of 1")
           print("")

    question2= input("Question 2 :- The power to decide an election petition is vested in the? \n a. Parliament\n b. Supreme Court\n c. High Courts\n d. Election Commission \n Answer :-")
    if question2=="c"or question2 =="High Courts":
       print("Correct")
       score =score +1
       print("Score is",score,"out of 2")
       print("")
    else:
       print("Incorrect answer is c, or High Court")
       print("Score is",score,"out of 2")
       print("")

    question3=input("Question 3 :-  The present Lok Sabha is the ?\n a. 14th Lok Sabha\n b. 15th Lok Sabha\n c. 16th Lok Sabha\n d. 17th Lok Sabha \n Answer :-")
    if question3 =="d" or question3 =="17th Lok Sabha ":
        print("Correct")
        score =score+1
        print("Score is",score,"out of 3")
        print ("")
    else:
       print ("Incorrect answer is c, or 17th Lok Sabha")
       print ("Score is",score,"out of 3")
       print ("")

    question4=input("Question 4 :- Who is the Current CM of Sikkim ? \n a. Shriniwas Dadasaheb Patil\n b. V.Rama Rao\n c. Prem Singh Tamang\n d. S.K. Bhatnagar\n Answer :-")
    if question4==  "c" or question4=="Prem Singh Tamang":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 4 ")
    else:
        print ("Incorrect answer is c, or Prem Singh Tamang")
        print("Score is ",score,"out of 4")
        print ("") 

    question5=input("Question 5 :- The total number of recognised official languages in Sikkim is ? \n a. 2\n b. 5\n c. 9\n d. 11\n Answer :-")
    if question5==    "d" or question5=="11":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 5 ")
    else:
        print ("Incorrect, answer is d or 11")
        print("score is ",score,"out of 5")
        print ("") 
    question6=input("Question 6 :-  Sikkim is the large exporter of ?\n a. Bamboo\n b. Chilly \n c. Cardamon \n d. None of the above\n Answer :-")
    if question6==    "c" or question6=="Cardamom":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 6")
    else:
        print ("Incorrect, answer is c  or Cardamom ")
        print("Score is ",score,"out of 6")
        print ("") 

    question7=input("Question 7 :- Which is the capital of Sikkim? \n a. Singtam\n b. Gangtok\n c. Mangan\n d. Rongphu\n Answer :-")
    if question7==    "b" or question7=="Gangtok":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 7 ")
    else:
        print ("Incorrect, answer is b  or Gangtok ")
        print("Score is ",score,"out of 7")
        print ("") 
    question8=input(" Question 8 :- How many Rajya Sabha seats in the state ? \n a. 10\n b. 9\n c. 8\n d .1\n Answer :-")
    if question8==    "d" or question8=="1":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 8 ")
    else:
        print ("Incorrect, answer is d  or 1 ")
        print("Score is ",score,"out of 8")
        print ("") 
    question9=input("Question 9 :- How many Lok sabha seats in the state?  \n a. 3\n b. 4\n c. 1\n d. 2\n Answer :-")
    if question9==    "c" or question9=="1":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 9 ")
    else:
        print ("Incorrect, answer is c  or 1 ")
        print("Score is ",score,"out of 9")
        print ("") 
    question10=input(" Question 10 :- Which is the Sikkim state animal ? \n a. Red Panda\n b. Camel\n c. Nilgiri Tahr\n d. Spotted deer\n Answer :-")
    if question10==    "a" or question10=="Red Panda":
        print ("Correct")
        score=score+1
        print("Score is ",score,"out of 10 ")
    else:
        print ("Incorrect, answer is a  or Red Panda ")
        print("Score is ",score,"out of 10")
        print ("") 
    stud.append(name)
    stud.append(admno)
    stud.append(classes)
    stud.append(score)
    ans=input("Anyone to give Quiz again???  Y/N")
    field.append(stud)
f=open("quiz.csv",'a',newline='')
c=csv.writer(f)
for i in field:
    c.writerow(i)
f.close()


