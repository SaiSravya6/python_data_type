# -*- coding: utf-8 -*-
"""day-3-assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/SaiSravya6/b404f6cfb10092d6cd5243a161107af9/day-3-assignment.ipynb
"""

subject1 = int(input("Enter the marks of subject1: "))
subject2 = int(input("Enter the marks of subject2: "))
subject3 = int(input("Enter the marks of subject3: "))
Average = subject1 + subject2 + subject3 / 3
if Average >= 90:
    print("GradeA")
elif Average > 80:
    print("GradeB")
elif Average >70:
    print(":GradeC")
else:
    print("Fail")