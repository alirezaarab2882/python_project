
def calculater(num1,num2):
    opp = input('please give me operator:\n+ - * /\n')
    
    if opp=='+':
        return (f'the pozitive of number is :{num1+num2}')
    elif opp=='-':
        return (f'the negetive of number is :{num1-num2}')
    elif opp=='*':
        return (f'the moltipluy of number is :{num1*num2}')
    elif opp=='/':
        return (f'the tagsim of number is:{num1/num2}')
    else:
        return ('the enter of operator is wrong')  
def again():
    calc_again = input(''' 
    do you like countinue???
    enter Y for Yes and enter N for No
    ''')    
    if calc_again.upper()=='Y':
       calculater()
    elif calc_again.upper()=='N':
        print('good bye')
    else:
        again()
print(calculater(int(input('enter of number 1:')),int(input('enter number of number2:'))))