#!/usr/bin/python3

#use input for rate and base_hours
#compute gross_pay

hours_worked = input('Enter hours :')
rate = input('Enter rate :')

if float(hours_worked) > 40:
    bonus_pay = (float(hours_worked) - 40) * (float(rate) * 1.5)
    regular_pay = (40 * float(rate))
    total_pay = bonus_pay + regular_pay
    print(total_pay)
else:
    regular_pay = (40 * float(rate))
    total_pay = regular_pay
    print(total_pay)
