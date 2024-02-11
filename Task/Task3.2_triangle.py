s1 = int(input("Enter the side 1:"))
s2 = int(input("Enter the side 2:"))
s3 = int(input("Enter the side 3:"))

if (s1 == s2 == s3):
    print("equilateral")
elif (s1 == s2 or s2 == s3 or s3 == s1):
    print("isosceles")
else:
    print("scalene")
