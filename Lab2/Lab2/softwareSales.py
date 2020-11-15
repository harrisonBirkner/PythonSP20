#This program asks the user to enter the number of packages purchased.
#The program then displays the amount of the discount (if any) and the total amount of the purchase after the discount.

qtyPackages = int(input('please input quantity of packages purchased: '))
total = qtyPackages * 99
if qtyPackages > 9 and qtyPackages < 20:
    discount = qtyPackages * 0.1
    print('Discount: $' + format(discount, '10,.2f'))
    print('Total after discount: $' + format(total - discount, '10,.2f'))
elif qtyPackages >= 20 and qtyPackages <= 49:
    discount = qtyPackages * 0.2
    print('Discount: $' + format(discount, '10,.2f'))
    print('Total after discount: $' + format(total - discount, '10,.2f'))
elif qtyPackages >= 50 and qtyPackages <= 99:
    discount = qtyPackages * 0.3
    print('Discount: $' + format(discount, '10,.2f'))
    print('Total after discount: $' + format(total - discount, '10,.2f'))
elif qtyPackages >= 100:
    discount = qtyPackages * 0.4
    print('Discount: $' + format(discount, '10,.2f'))
    print('Total after discount: $' + format(total - discount, '10,.2f'))
else:
    discount = 0
    print('Discount: $' + format(discount, '10,.2f'))
    print('Total after discount: $' + format(total - discount, '10,.2f'))
