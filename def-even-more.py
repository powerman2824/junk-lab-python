def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        x = 0
        while num_cycles != x:
            x = x + 1
            print(f'{x} : Lather and rinse.')
        print('Done.')

user_cycles = int(input())
shampoo_instructions(user_cycles)