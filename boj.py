# 단계별 분류
# 1단계 - 입출력과 사칙연산
# 2557
# print("Hello World")

# 10718
# print('강한친구 대한육군')
# print('강한친구 대한육군')

# 10171
# print('\\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

# 10172
# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|\"^\"`    |')
# print('||_/=\\\\__|')

# 1000, 1001, 10998, 1008
# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# 10869
# A, B = map(int, input().split())
# print(A + B)
# print(A - B)
# print(A * B)
# print(int(A / B))
# print(A % B)

# 10926
# id = input()
# print(id + '??!')

# 18108
# y = int(input())
# print(y - 543)

# 10430
# A, B, C = map(int, input().split())
# print((A+B) % C)
# print(((A % C) + (B % C)) % C)
# print((A*B) % C)
# print(((A % C) * (B % C)) % C)

# 2588
# a = int(input())
# b = int(input())
# for i in reversed(range(len(str(b)))):
#     print(int(str(b)[i]) * a)
# print(a * b)

# 1330
# A, B = map(int, input().split())
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')

# 9498
# score = int(input())
# if score <= 100 and score >= 90:
#     print('A')
# elif score <= 89 and score >= 80:
#     print('B')
# elif score <= 79 and score >= 70:
#     print('C')
# elif score <= 69 and score >= 60:
#     print('D')
# else:
#     print('F')

# 2753
# year = int(input())
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print(1)
# else:
#     print(0)

# 14681
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

# 2884
# H, M = map(int, input().split())
# if H != 0 and M < 45:
#     print(H - 1, 15 + M)
# elif H == 0 and M < 45:
#     print(23, 15 + M)
# else:
#     print(H, M - 45)

# 2525 => n 공식이 정말 혁명적인 공식
# A, B = map(int, input().split())
# C = int(input())
# n = (B + C) // 60  # 몫
# if A + n > 23:
#     print((A + n) % 24, (B + C) % 60)
# else:
#     print(A + n, (B + C) % 60)

# 2480 => set함수, list함수, sum함수 알게됨
# a, b, c = map(int, input().split())
# arr = [a, b, c]
# arr_set = list(set(arr))
# arr_set_length = len(arr_set)
# if arr_set_length == 1:
#     print(10000 + (1000 * arr_set[0]))
# elif arr_set_length == 2:
#     print(1000 + (100 * (sum(arr) - sum(arr_set))))
# else:
#     print(100 * max(arr))

# 2438
# N = int(input())
# for i in range(N):
#     print('*'*(i+1))

# 2439
# N = int(input()) ==> solution 1
# for i in range(N):
# print(f"{'*' * (i + 1):>{N}}")

# N = int(input()) ==> solution 2
# for i in range(N):
#     print(('*'*(i+1)).rjust(N))

# 2440
# N = int(input())
# for i in reversed(range(N)):
#     print('*' * (i + 1))

# 2441
# N = int(input())
# for i in reversed(range(N)):
#     print(('*' * (i + 1)).rjust(N))

# 2442
# N = int(input())
# for i in range(N):
#     print(('*' * (i + 1)).rjust(N) + ('*' * i)) ==> space fnc loops
# print((' ' * (i)) + ('*' * (N - i)) + ('*' * (N - i - 1))) ==> reversed loops
# print((' ' * (N - i - 1)) + ('*' * ((2 * (i + 1)) - 1))) ==> kcj's king god general solution(no reverse)

# 2443
# N = int(input())
# for i in range(N):
#     print(('*' * (N - i)).rjust(N) + ('*' * (N - i - 1)))

# 2739
# N = int(input())
# for i in range(9):
#     print(f'{N} * {i + 1} = {N * (i + 1)}')

# 10950
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print(A + B)

# 8393
# n = int(input())
# initial_num = 0
# for i in range(n):
#     initial_num += i + 1
# print(initial_num)

# 15552
# import sys
# T = int(sys.stdin.readline().rstrip())
# for i in range(T):
#     [A, B] = map(int, sys.stdin.readline().split()) => [A, B] 를 A, B 로 바꿔줘도 됨. A, B라고 해도 파이썬이 리스트로 인식하는 것 같음.
#     print(A + B)

# 2741
# N = int(input())
# for i in range(N):
#     print(i + 1)

# 2742
# N = int(input())
# for i in reversed(range(N)):
#     print(i + 1)

# 11021
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print(f"Case #{i + 1}: {A + B}")

# 11022
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print(f"Case #{i + 1}: {A} + {B} = {A + B}")

# 10952
# while True:
#     A, B = map(int, input().split())
#     if A != 0 and B != 0:
#         print(A + B)
#     else:
#         break

# 10951
# from sys import stdin
# while True:
#     try:
#         A, B = map(int, stdin.readline().split())
#     except:
#         break
#     else:
#         print(A + B)

# 2562
# arr = []
# for i in range(9):
#     n = int(input())
#     arr.append(n)
# print(max(arr))
# print(arr.index(max(arr)) + 1)

# 2577
# A = int(input())
# B = int(input())
# C = int(input())
# Time = str(A * B * C)
# for i in range(10):
#     print(Time.count(f'{i}'))

# 3052
# arr = []
# for i in range(10):
#     a = int(input())
#     arr.append(a % 42)
# print(len(set(arr)))

# 1152
# Paragraph = input()
# print(len(Paragraph.split()))

# 10871
# import sys
# N, X = map(int, sys.stdin.readline().split())
# A = list(map(str, input().split()))
# under = []
# for i in range(N):
#     if len(A) == N:
#         try:
#             if int(A[i]) < X:
#                 under.append(A[i])
#         except:
#             break
#     else:
#         break
# print(' '.join(under))

# 1110 ==> 정수형으로 한번 더풀어보기!
# N = input()
# arr = []
# if len(N) == 1:
#     N = '0' + N[0]
# arr.append(N[1] + str(int(N[0]) + int(N[1]))[-1])
# while arr[-1] != N:
#     arr.append(arr[-1][1] + str(int(arr[-1][0]) + int(arr[-1][1]))[-1])
# print(len(arr))
# N = input()
# arr = []
# if len(N) == 1:
#     arr.append(N[0] + N[0])
# else:
#     arr.append(N[1] + str(int(N[0]) + int(N[1]))[-1])
# while arr[-1] != N:
#     if len(str(int(arr[-1][0]) + int(arr[-1][1]))) == 1:
#         arr.append(arr[-1] + arr[-1])
#     else:
#         arr.append(arr[-1][1] + str(int(arr[-1][0]) + int(arr[-1][1]))[-1])
# print(arr)

# 10818
# N = int(input())
# X = list(map(int, input().split()))
# if len(X) == N:
#     print(min(X), max(X))

# 1546
# N = int(input())
# X = list(map(int, input().split()))
# if len(X) == N:
#     score = 0
#     for i in range(N):
#         score += ((X[i]/max(X)) * 100)/N
# print(score)

# 15596
# import sys
# a = list(map(int, sys.stdin.readline().split()))
# def solve(a):
#     ans = 0
#     for i in range(len(a)):
#         ans += a[i]
#     return ans

# 11720
# N = int(input())
# A = list(map(int, input()))
# if len(A) == N:
#     sum = 0
#     for i in range(N):
#         sum += A[i]
#     print(sum)

# 2558
# A = int(input())
# B = int(input())
# print(A+B)

# 10872
# N = int(input())
# fact = 1
# for i in range(N):
#     fact *= (i+1)
# print(fact)

# 10953
# N = int(input())
# for i in range(N):
#     A, B = map(int, input().split(','))
#     print(A+B)

# 10757
# A, B = map(int, input().split())
# print(A+B)

# 15792
# A, B = map(int, input().split())
# print(A/B)

# 2576
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
# F = int(input())
# G = int(input())
# arr = [A, B, C, D, E, F, G]
# arr2 = []
# for i in range(7):
#     if arr[i] % 2 != 0:
#         arr2.append(arr[i])
# if len(arr2) == 0:
#     print(-1)
# else:
#     print(sum(arr2))
#     print(min(arr2))

# 10886
# N = int(input())
# survey = []
# for i in range(N):
#     vote = int(input())
#     survey.append(vote)
# if survey.count(0) > survey.count(1):
#     print('Junhee is not cute!')
# else:
#     print('Junhee is cute!')

# 8958
# N = int(input())
# for i in range(N):
#     Q = list(map(str, input()))
#     score = 0
#     arr = []
#     for q in range(len(Q)):
#         if Q[q] == 'O' or Q[q] == 'X':
#             if Q[q] == 'X':
#                 score = 0
#             else:
#                 score += 1
#                 arr.append(score)
#         else:
#             break
#     print(arr)

# 4344 ==> 잘 나오는데 왜 틀린걸까....
# C = int(input())
# for i in range(C):
#     N = list(map(int, input().split()))
#     if N[0] == len(N[1:]) and N[0] != 0:
#         mean = sum(N[1:])/N[0]
#         st_above_mean = 0
#         for s in range(len(N[1:])):
#             if N[1:][s] > mean:
#                 st_above_mean += 1
#         apart = str(round((st_above_mean/N[0])*100, 3)).split('.')
#         print(f'{apart[0]}.{apart[1].ljust(3,"0")}%')
#     else:
#         break

# 11654
# A = input()
# if len(A) == 1:
#     print(ord(A))

# 10809
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# S = input()
# word = ''
# for i in range(len(alphabet)):
#     if alphabet[i] in S:word += str(S.index(alphabet[i])) + ' '
#     else:word += '-1 '
# print(word)

# 2675
# T = int(input())
# if T >= 1 and T <= 1000:
#     for i in range(T):
#         R, B = map(str, input().split())
#         word = ''
#         for w in range(len(B)):
#             word += B[w] * int(R)
#         print(word)

# 2908
# A, B = map(int, input().split())
# arr = [int(str(A)[::-1]), int(str(B)[::-1])]
# print(max(arr))

# 4504
# n = int(input())
# while True:
#     numb = int(input())
#     if numb != 0:
#         if numb % n != 0:
#             print(f'{numb} is NOT a multiple of {n}.')
#         else:
#             print(f'{numb} is a multiple of {n}.')
#     else:
#         break

# 3046
# R1, S = map(int, input().split())
# R2 = 2 * S - R1
# print(R2)

# 2163
# N, M = map(int, input().split())
# print(N * M - 1)

# 10699
# from datetime import datetime, timedelta
# print(str(datetime.today() + timedelta(hours=9))[:10])

# 7287
# print(63)
# print('qkrdlswo98')

# 2530
# A, B, C = map(int, input().split())
# D = int(input())
# if (A >= 0 and A < 24) and (B >= 0 and B < 60) and (C >= 0 and C < 60) and (D >= 0 and D < 500000):
#     C += (D % 60)
#     B += (D // 60)
#     if C > 59:
#         B += 1
#         C %= 60
#     if B > 59:
#         A += (B // 60)
#         B %= 60
#     if A > 23:
#         A %= 24
#     print(A, B, C)

# 2914
# A, I = map(int, input().split())
# print(A * (I - 1) + 1)

# 5355
# T = int(input())
# for t in range(T):
#     N = list(map(str, input().split()))
#     if '.' in N[0]:
#         N_first = float(N[0])
#     else:
#         N_first = int(N[0])
#     for n in range(1, len(N)):
#         if N[n] == '@':
#             N_first *= 3
#         elif N[n] == '%':
#             N_first += 5
#         elif N[n] == '#':
#             N_first -= 7
#     print("{:.2f}".format(N_first)) ==> round함수의 한계점

# 10817
# A, B, C = map(int, input().split())
# arr_sort = sorted([A, B, C])
# print(arr_sort[1])

# 4101
# while True:
#     A, B = map(int, input().split())
#     if A != 0 and B != 0:
#         if A > B:
#             print('Yes')
#         else:
#             print('No')
#     else:
#         break

# 10102
# V = int(input())
# R = input()
# A = 0
# B = 0
# for i in range(len(R)):
#     if R[i] == 'A':
#         A += 1
#     else:
#         B += 1
# if A > B:
#     print('A')
# elif A == B:
#     print('Tie')
# else:
#     print('B')

# 2935
# A = input()
# T = input()
# B = input()
# A_pow = len(A[1:])
# B_pow = len(B[1:])
# if T == '*':
#     print(10**(A_pow + B_pow))
# else:
#     print(int(A) + int(B))

# 11653
# N = int(input())
# n = 1
# while N - n != 0:
#     n += 1
#     if N % n == 0:
#         print(n)
#         N = N/n
#         n = 1

# 1789
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
# arr = [A, B, C, D, E]
# for i in range(len(arr)):
#     if arr[i] < 40:
#         arr[i] = 40
# print(int(sum(arr)/5))

# 1934
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     A_origin = A
#     B_origin = B
#     a = 1
#     b = 1
#     arr_a = []
#     arr_b = []
#     arr_ab = []
#     while A - a != 0:
#         a += 1
#         if A % a == 0:
#             arr_a.append(a)
#     while B - b != 0:
#         b += 1
#         if B % b == 0:
#             arr_b.append(b)
#     for s in range(len(arr_a)):
#         if arr_a[s] in arr_b:
#             arr_ab.append(arr_a[s])
#     if len(arr_ab) == 0:
#         print(A_origin * B_origin)
#     else:
#         print(int((A_origin*B_origin)/arr_ab[-1]))

# 9506
# while True:
#     n = int(input())
#     n_origin = n
#     arr = ['1']
#     i = 1
#     if n != -1:
#         while n - i != 0:
#             i += 1
#             if n % i == 0:
#                 arr.append(str(i))
#         arr_int = map(int, arr)
#         integrate = sum(arr_int) - n_origin
#         if integrate != n_origin:
#             print(f'{n_origin} is NOT perfect.')
#         else:
#             print(f'{n_origin} = {" + ".join(arr[:-1])}')
#     else:
#         break

# 1789
# S = int(input())
# arr = []
# i = 0
# while sum(arr) + i < S:
#     i += 1
#     arr.append(i)
# print(len(arr))

# 9610
# n = int(input())
# Q1 = 0
# Q2 = 0
# Q3 = 0
# Q4 = 0
# AXIS = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x*y > 0:
#         if x > 0 and y > 0:
#             Q1 += 1
#         else:
#             Q3 += 1
#     elif x*y < 0:
#         if x > 0 and y < 0:
#             Q4 += 1
#         else:
#             Q2 += 1
#     else:
#         AXIS += 1
# print(f'Q1: {Q1}')
# print(f'Q2: {Q2}')
# print(f'Q3: {Q3}')
# print(f'Q4: {Q4}')
# print(f'AXIS: {AXIS}')

# 10988
# word = input()
# if word == word[::-1]:
#     print(1)
# else:
#     print(0)

# 5717
# while True:
#     M, F = map(int, input().split())
#     if M != 0 and F != 0:
#         print(M + F)
#     else:
#         break

# 2754
# dick = {
#     'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
#     'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
#     'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
#     'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
#     'F': 0.0
# }
# score = input()
# print(dick[score])

# 10103
# n = int(input())
# a_score, b_score = 100, 100
# for i in range(n):
#     a, b = map(int, input().split())
#     if a > b:
#         b_score -= a
#     elif a < b:
#         a_score -= b
# print(a_score)
# print(b_score)3

# 2476
# N = int(input())
# price = []
# for i in range(N):
#     D = list(map(int, input().split()))
#     D_set = list(set(sorted(D)))
#     if len(D_set) == 3:
#         price.append(D_set[2]*100)
#     elif len(D_set) == 2:
#         D.remove(D_set[0])
#         D.remove(D_set[1])
#         price.append(1000 + (D[0] * 100))
#     else:
#         price.append(10000 + (D_set[0] * 1000))
# print(max(price))

# 3009
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# arr_x = sorted([A[0], B[0], C[0]])
# arr_y = sorted([A[1], B[1], C[1]])
# non_x = (2 * arr_x[0]) + (2 * arr_x[-1]) - sum(arr_x)
# non_y = (2 * arr_y[0]) + (2 * arr_y[-1]) - sum(arr_y)
# print(non_x, non_y)

# 5063
# N = int(input())
# for i in range(N):
#     r, e, c = map(int, input().split())
#     if r + c < e:
#         print('advertise')
#     elif r + c == e:
#         print('does not matter')
#     else:
#         print('do not advertise')

# 7567
# dish = input()
# height = 10
# for i in range(0, len(dish)-1):
#     if dish[i+1] == dish[i]:
#         height += 5
#     else:
#         height += 10
# print(height)

# 10214
# T = int(input())
# for _ in range(T):
#     Y = K = 0
#     for _ in range(9):
#         y, k = map(int, input().split())
#         Y += y
#         K += k
#     if Y > K:
#         print('Yonsei')
#     elif Y < K:
#         print('Korea')
#     else:
#         print("Draw")

# 11557
# T = int(input())
# for i in range(T):
#     N = int(input())
#     arr_s = []
#     arr_d = []
#     for s in range(N):
#         S, D = map(str, input().split())
#         arr_s.append(S)
#         arr_d.append(int(D))
#         max_d = max(arr_d)
#         index = arr_d.index(max_d)
#     print(arr_s[index])

# 10181
# while True:
#     n = int(input())
#     n_origin = n
#     arr = ['1']
#     i = 1
#     if n != -1:
#         while n - i != 0:
#             i += 1
#             if n % i == 0:
#                 arr.append(str(i))
#         arr_int = map(int, arr)
#         integrate = sum(arr_int) - n_origin
#         if integrate != n_origin:
#             print(f'{n_origin} is NOT perfect.')
#         else:
#             print(f'{n_origin} = {" + ".join(arr[:-1])}')
#     else:
#         break

# 2750
# N = int(input())
# arr = []
# for i in range(N):
#     n = int(input())
#     arr.append(n)
# arr_s = sorted(arr)
# for s in range(N):
#     print(arr_s[s])

# 2752
# A, B, C = map(int, input().split())
# arr = [A, B, C]
# for i in range(3):
#     print(sorted(arr)[i], end=' ')

# 5800
K = int(input())
for i in range(K):
    arr_gap = []
    N = list(map(int, input().split()))
    arr_sort = sorted(N[1:])
    for s in range(len(arr_sort)):
        arr_gap.append(arr_sort[i+1]-arr_sort[i])
    print(f'Class {i+1}')
    print(f'Max {arr_sort[-1]}, Min {arr_sort[0]}, Largest gap {max(arr_gap)}')

# 시간초과, 메모리초과 모음집

# 10989 => 메모리초과
# import sys
# n = int(sys.stdin.readline())
# b = [0] * 10001
# for i in range(n):
#     b[int(sys.stdin.readline())] += 1
# for i in range(10001):
#     if b[i] != 0:
#         for j in range(b[i]):
#             print(i)

# 10815 => 시간초과
# from sys import stdin
# N = int(stdin.readline())
# get = list(map(int, stdin.readline().split()))
# M = int(stdin.readline())
# suggest = list(map(int, stdin.readline().split()))
# for i in range(M):
#     if suggest[i] in get:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# 1837 => 시간초과
# from math import ceil
# P, K = map(int, input().split())
# i = ceil(P**(1/2))
# m = 1
# while True:
#     i -= m
#     if P % i == 0:
#         break
# if i < K:
#     print('BAD', i)
# else:
#     print('GOOD')
