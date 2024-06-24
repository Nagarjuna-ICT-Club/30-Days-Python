def number_type(num):
    match num:
        # Matches every case where number is
        # greater than 0
        case _ if num > 0:
            return "Positive"

        case 0:
            return "Zero"
            
        # Matches every case where number is
        # less than 0
        case _ if num < 0:
            return "Negative"

print(number_type(5))
print(number_type(-27))
print(number_type(0))
