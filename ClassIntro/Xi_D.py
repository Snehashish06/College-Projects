"""      Coded by Snehashish and Pradumya!!  """
def class_Xi_D(bool, *args, **kwargs) -> str:
    if bool != True:
        return
    stream = "Commerce"
    class_ = "Xi D"
    class_teacher = "Rk Mehra"
    class_captain = ("Snehashish Biswas", "Priyu Singh")
    i = [x for x in range(43)]
    all_info = [class_, f"{i[-1]}", f"{stream}", class_teacher]
    all_info.extend(class_captain)
    str = f"""We are the students of class: {all_info[0]},
              our class teacher is: {all_info[3]},
              strength of our class is: {all_info[1]},
              we are {all_info[2]} students, 
              our class captains are: {all_info[4]}, {all_info[5]}..."""
    return str

print(f"{class_Xi_D(True)}\n\n{__doc__}")
