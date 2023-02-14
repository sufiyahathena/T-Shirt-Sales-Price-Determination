#Control Structures
#Sufiyah Sajan
#Part A

shirtquote = input("Enter the quote you would like printed on the T-shirts: ")
shirtamount = input("How many T-Shirts would you like to have printed? ")
shirtcolor = input("How many colors will each shirt be printed with (1, 2, or 3)? ")

if shirtcolor == 1 and shirtamount < 99:
    price = 8 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 1 and shirtamount > 99 and shirtamount < 249:
    price = 6 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 1 and shirtamount > 250:
    price = 5 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 2 and shirtamount < 99:
    price = 9 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 2 and shirtamount > 99 and shirtamount < 249:
    price = 7 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 2 and shirtamount > 250:
    price = 6 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 3 and shirtamount < 99:
    price = 10 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
elif shirtcolor == 3 and shirtamount > 99 and shirtamount < 249:
    price = 8 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)
else:
    price = 7 * float(shirtamount)
    taxprice = 0.08875 * float(price)
    totalprice = float(price) + float(taxprice)
    total = format(totalprice, '.2f')
    print(shirtamount, " shirts screen printed with ", shirtcolor, " colors: $", total)


