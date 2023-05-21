# Defining the function/method finding the maximum steps
def Bat_programmer(patient,steps):
    # Returning the maximum steps required
    return patient * steps

patient = eval(input()) # Taking input the number of patient
steps = eval(input()) # Taking input the number of steps already covered

# Printing the maximu steps
print(Bat_programmer(patient,steps))
