def find_temp(temp):
    # Set an initial message
    message = "Normal Temperature"
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever"
    return message
    
print(find_temp(20))



def else_temp(temp):
    if temp > 38:
        message = "Fever! "
    else:
        message = "Normal Temperature "
    return message

print(else_temp(45))


def elif_temp(temp):
    if temp > 38:
        message = "Fever "
    elif temp > 35:
        message = "Normal Temperature "
    else:
        message = "Low Temperature "
    return message

print(elif_temp(34))
