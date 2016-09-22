#!/usr/bin/python
name = raw_input("What's your name? ")
print("Hello, " + name + ".")
print("Nice to meet you " + name + "!")
grade = input("Please enter your numberic grader: ")

if grade >= 90:
	print("Nicely done!")
	letterGrade = 'A'
elif grade >= 80:
	letterGrade = 'B'
elif grade >= 70:
	letterGrade = 'C'
elif grade >= 60:
	letterGrade = 'D'
else:
	print("I am sorry to inform you: ")
	letterGrade = 'F'
print("You earned a(n) " + letterGrade + ".")

