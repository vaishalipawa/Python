Indian = ["samosa", "medu vada", "kachori", "paratha"]
Chinise = ["chiken fry", "egg roll", "noodles"]
Italian = ["pazza", "Pasta", "risotto"]
dish = input("Enter a dish name :")
if dish in Indian:
    print("dish is indian")
elif dish in Chinise:
    print("the dish is chinise")
elif dish in Italian:
    print("the dish is italian")
else:
    print("i dont know which dish is this", dish)    
