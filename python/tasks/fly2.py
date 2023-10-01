n = int(input())
seats = [[i for i in input()] for _ in range(n)]

m = int(input())
passengers = [input().split() for _ in range(m)]
passengers2 = [[] for _ in range(m)]
# place2 = 'ABCDEF'
for i in range(m):
    if passengers[i][1] == 'left':
        if passengers[i][2] == 'aisle':
            # passengers2[i].append(place2[-3-int(passengers[i][0]):3])
            passengers2[i] = list(range(3 - int(passengers[i][0]), 3))
        else:
            # passengers2[i].append(place2[:4-int(passengers[i][0])])
            passengers2[i] = list(range(0, int(passengers[i][0])))
    if passengers[i][1] == 'right':
        if passengers[i][2] == 'aisle':
            # passengers2[i].append(place2[4:4+int(passengers[i][0])])
            passengers2[i] = list(range(4, 4 + int(passengers[i][0])))
        else:
            # passengers2[i].append(place2[6-int(passengers[i][0]):6])
            passengers2[i] = list(range(7 - int(passengers[i][0]), 7))
    # passengers2[i] = ''.join(passengers2[i])

print(passengers2)
# print(list(range(2, -2 + int(passengers[0][0]), -1)))
for i in range(n):
    print(''.join(seats[i]))
print()

print(seats)