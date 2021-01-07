def print_gugudan(a):
    if type(a)==int and 1<= a <=9:
        for i in range(1, 10):
            print('%d * %d = %d'%(a,i,a * i))
    else:
        pass

print_gugudan(2)
print('\n')
print_gugudan(3)
print('\n')
print_gugudan(4)
print('\n')
print_gugudan(20)