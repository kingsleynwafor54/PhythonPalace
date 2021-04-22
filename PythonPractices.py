def name_age_display():
    student = []
    for counter in range(3):
        name_str = input("enter your name: ")
        age_int = int(input("enter age: "))
        student.append((name_str,age_int))

    return student



print(name_age_display())