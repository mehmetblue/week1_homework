"""
Name, Surname, Student Number, 4 course names, Midterm and Final grades of these courses will be requested from the user.
The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average. Average;
     If it is less than 50, “FAILED” on the screen,
     If it is 50 and above, “PASSED” will be printed on the screen.
     This printing process will be done in 4 lessons and the lessons will be printed one after the other.
"""
name = input("Name: ")
sur_name = input("Surname: ")
student_number = input("Student Number: ")

les_1 = input("Lesson 1: ")
les_1_midterm = int(input(f"{les_1} Midterm Score: "))
les_1_final = int(input(f"{les_1} Final Score: "))

les_2 = input("Lesson 2: ")
les_2_midterm = int(input(f"{les_2} Midterm Score: "))
les_2_final = int(input(f"{les_2} Final Score: "))

les_3 = input("Lesson 3: ")
les_3_midterm = int(input(f"{les_3} Midterm Score: "))
les_3_final = int(input(f"{les_3} Final Score: "))

les_4 = input("Lesson 4: ")
les_4_midterm = int(input(f"{les_4} Midterm Score: "))
les_4_final = int(input(f"{les_4} Final Score: "))

score_les1 = (les_1_midterm * 0.4) + (les_1_final * 0.6)
score_les2 = (les_2_midterm * 0.4) + (les_2_final * 0.6)
score_les3 = (les_3_midterm * 0.4) + (les_3_final * 0.6)
score_les4 = (les_4_midterm * 0.4) + (les_4_final * 0.6)

print(f"{student_number} - {name} {sur_name}'s Lesson Situations: ")

if score_les1 >= 50:
    print(f"{les_1}: PASSED")
else:
    print(f"{les_1}: FAILED")

if score_les2 >= 50:
    print(f"{les_2}: PASSED")
else:
    print(f"{les_2}: FAILED")

if score_les3 >= 50:
    print(f"{les_3}: PASSED")
else:
    print(f"{les_3}: FAILED")

if score_les4 >= 50:
    print(f"{les_4}: PASSED")
else:
    print(f"{les_4}: FAILED")
