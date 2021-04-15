#Написать функцию которая аргументом принимает число и выдает это количество
# четных чисел фибоначчи 
def f(n):
    try:
        N = int(n)
        fib_n1 = 1
        fib_n2 = 1
        text = '0'
        while N > 1:
            sum_fib = fib_n1 + fib_n2
            if sum_fib%2 == 0:
                N-=1
                text+=f', {str(sum_fib)}'
            fib_n1 = fib_n2
            fib_n2 = sum_fib
        return(text)
    except:
        return('Введите число')

  
n = input()
print(f(n))
