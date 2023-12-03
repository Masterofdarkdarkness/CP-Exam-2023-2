T = int(input())
cont = 0
case_number = 1

if T < 1 or T > 100:
    print('ERROR')
else:
    while cont < T:
        N = input().split()
        y = int(N[0])

        if y != len(N) - 1:
            middle = "ERROR"
        else:
            middle = N[y // 2 + 1]

        print(f'Case {case_number}: {middle}')
        cont += 1
        case_number += 1
