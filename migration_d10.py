from random import randint

results_of_d10s = []
summed_d10s = []

def push(value):
    summed_d10s.append(f"{value}")
    results_of_d10s.append(value)

def d_10():

    definer = randint(1, 3)
    selector = randint(1, 4)
    # -> Weak rolls :(
    if definer == 1:
        # => Weakest roll
        if selector == 1 or 2:
            d10 = randint(1, 4)
            push(d10)
        
        # => Weak roll
        if selector == 3:
            d10 = randint(2, 5)
            push(d10)

        # => Raw roll
        if selector == 4:
            d10 = randint(1, 10)
            push(d10)
    #====================================#
    # -> Medium rolls :|
    elif definer == 2:
        if selector == 1:
            d10 = randint(4, 1)
            push(d10)
    
    else:
        result = randint(10, 20)
        results_of_d10s.append(result)

    print(results_of_d10s)

text_input = ''

while text_input != '0':
    text_input = input('Insira um número!')
    d_10()
