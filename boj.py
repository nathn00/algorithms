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

# 10950

# 8393

# 15552

# 2741

# 2742

# 11021

# 11022

# 2438

# 2439

# 10871

# 10952

# 10951

# 1110
