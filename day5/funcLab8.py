def print_triangle_withdeco(a,b='%'): #b기본값은 %
    if 1<=a<=10:
        for i in range(1,a+1):
            print(' '*(a-i),b * i)
    else: pass

print_triangle_withdeco(3,'*')
print_triangle_withdeco(5, '^')
print_triangle_withdeco(6)
print_triangle_withdeco(13)