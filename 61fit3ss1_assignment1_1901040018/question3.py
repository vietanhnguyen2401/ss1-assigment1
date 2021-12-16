low = 1
high = 100
print('Please pick a random number in 1 to 100 and keep it secret. I will try to guess your number!')
count = 0
while True:
    count+=1
    guess = (high + low)//2
    print('Is ' + str(guess) + ' your number?')
    a = raw_input ("Enter 'c' if is correct. Enter 'h' if my guess number is bigger than you. Otherwise enter 'l' ")
    if a == 'c':
        print('I did it in '+ str(count)+' try')
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')