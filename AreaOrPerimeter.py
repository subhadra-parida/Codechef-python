L=int(input("Enter any number="))
B=int(input("Enter any number="))
Area=L*B
Perimeter=2*(L+B)
if (Area > Perimeter):
    print("Area")
    print(Area)
elif (Area < Perimeter):
    print("Perimeter")
    print(Perimeter)
else:
    print("Eq")
    # print(Equal)

    