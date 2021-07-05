
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are male but are short")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are neither male nor tall")

