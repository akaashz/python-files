total_units, peak_units, consumer = input().split()

total_units = int(total_units)
peak_units = int(peak_units)

if total_units == 0:
    print(0)

else:

    if consumer == "H":

        if total_units <= 100:
            bill = total_units * 3

        elif total_units <= 300:
            bill = 100 * 3 + (total_units - 100) * 5

        else:
            bill = 100 * 3 + 200 * 5 + (total_units - 300) * 8

    else:

        if total_units <= 100:
            bill = total_units * 5

        elif total_units <= 300:
            bill = 100 * 5 + (total_units - 100) * 8

        else:
            bill = 100 * 5 + 200 * 8 + (total_units - 300) * 12

    if peak_units > total_units * 0.4:
        bill = int(bill * 1.15)

    print(bill)