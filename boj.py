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

# 5622 ==> 보류!
# from string import ascii_lowercase
# alphabet_list = list(ascii_lowercase)
# W = input()
# arr = []
# for i in range(len(alphabet_list)):
#     alphabet = ''
#     for w in range(len(W)):
#         if alphabet_list[i] == W[w].lower():
#             alphabet += alphabet_list[i]
#     arr.append(alphabet)
# set_list = list(set(arr))[1::]
# sorted_arr = sorted(set_list, key=lambda x: len(x))
# print(sorted_arr)

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
