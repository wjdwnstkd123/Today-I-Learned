a = [12, 23, 43, 55, 66, 77]

print('1.')
small = a[0]

print('\n2.')
for i in a:
    if i < small:
        small = i
print(small)     

big = a[5]
print('\n3.')
for i in a:
    if i < big:
        big = i
print(big)   

print('\n4.')
print(min(a))

print('\n5.')
print(max(a))

print('\n6.')
print(sum(a))

print('\n7.')
b = [i+5 for i in range(20)]
print(b)

print('\n8.')
c = [i*2 for i in range(10)]
print(c)

print('\n9.')
d = [i for i in range(10) if i % 2 == 0]
print(d)

print('\n10.') #정수 부분만 출력
a = [1.2,3.4,4.5,2.7,5.1]
a = list(map(int, a))
print(a)

print('\n11.')
# a = input().split()
# print(a)

print('\n12.')#배열에 정수 넣기
print(list(a))
# a = map(int, input().split())
# print(list(a))

print('\n13.')# 배열에 소수 넣기
a = map(float, input().split())


