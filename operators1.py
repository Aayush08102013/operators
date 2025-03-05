# arithmatic operators:
tree1 = 82
tree2 = 94.7
tree3 = 22.98
tree4 = 54.9
tree5 = 100.78
sum = tree1 + tree2 + tree3 + tree4 + tree5
avg_hight = sum / 5
print(f"The average tree hiehgt is {avg_hight}")
# to find the toltal number of denominations
amt = int(input("enter your amount of money: "))
notes_of_1000 = amt//1000
notes_of_100 = (amt%1000)//100
notes_of_50 = (amt%100)//50
notes_of_10 = ((amt%100)%50)//10
print(f"the amount of notes of 1000 is: {notes_of_1000} thousands")
print(f"the amount of notes of 100 is: {notes_of_100} hundreds")
print(f"the amount of notes of 50 is: {notes_of_50} fivtys")
print(f"the amount of notes of 10 is: {notes_of_10} tens")
# find the percentage of marks obtained by a student
print("enter marks obtained for 3 subjects")
inp_maths =  int(input("maths: "))
inp_science = int(input("science: "))
inp_social = int(input("social: "))
sum_sub = inp_maths + inp_science + inp_social
avg_sum = sum_sub / 3
print(f"the average obtained by students are:{avg_sum}") 
perc = (avg_sum)*100
print(end="the percentage of marks obtained by the students are:")
print(perc)
