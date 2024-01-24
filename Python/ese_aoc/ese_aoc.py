def read_number(filename: str) -> float:
    f = open(filename, 'r')
    lst = []
    val = 0
    d = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for line in f:
        for c in line:
            if c in d:
                lst.append(c)

        num1 = lst[0] 

        if len(lst) > 1:
            num2 = lst[len(lst)-1]
        elif len(lst) == 1:
            num2 = num1
        if num1 in d and num2 in d:
            val += int(num1+num2)
        elif num1 in d:
            val += int(num1)
        elif num2 in d:
            val += int(num2)
        lst = []
    return val


def read_number_01(filename: str) -> float:
    f = open(filename, 'r')
    nums = {str(i):str(i) for i in range(0,10)}
    rep1 =  {'one': '1', 'two': '2', 'three': '3', 'for' : '4', 'five' : '5', 'six': '6', 'seven' : '7', 'eight': '8', 'nine': '9'}
    
    ret = 0
    for line in f.split():
        for k,v in rep1.items():
            line = line.replace(k, k+v+k) #per ogni chiave e quindi numero del dizionario, se lo trovo lo sostituisco con la chiave+numero+chiave
                                          #faccio questa sostituzione a somma perchè cosi se ho due parole sovrapposte non mi perdo la seconda sostituendo la prima scritta col numero
        curr = ''
        for c in line:
            if c in nums.keys():
                curr += nums#da completaree!!! vedere se lo carica online!!
                break



        



v = read_number_01('/home/ute/Scrivania/Python/ese_aoc/input.txt')
print(v)