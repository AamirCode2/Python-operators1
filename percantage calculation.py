print("Enter marks obtained in math, english, science and hindi \n")

math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("\nSum of math, english, science and hindi is", sum,"\n")

perc = (sum/400)*100

print(end="Percentage mark is ")
print(perc)