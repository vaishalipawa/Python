def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

toms_exp_list = [1, 6, 6, 3]
joe_exp_list = [485,8960,5869, 9870] 

toms_total = calculate_total(toms_exp_list)
joes_total = calculate_total(joe_exp_list)

print("toms expenses is : ", toms_total)
print("joes expenses is : " , joes_total)    
    