'''
리스트 List
- 대괄호로 표기
- 빈 리스트 존재한다.
'''
my_list_1 = []
# 어떤 자료형도 저장할 수 있다. 
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!']]

print(my_list_2[1])  #a

print(my_list_2[:3]) #처음부터
# [1, 'a', 3]

print(len(my_list_3)) #5
print(my_list_3[4][-1])



'''
range
연속된 정수 시퀀스를 생성하는 *변경 불가능한* 자료형
'''

my_range_1 = range(5)
my_range_2 = range(1,10)

print(my_range_1) # range(0,5)
print(my_range_2) # range(1,10)
# 활용법
print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 딕셔너리 (중복이 불가능)

my_dict = {'apple': 12, 'list': [1, 2, 3], 'apple': 100} # key 'apple' 이 중복되었다. 
print(my_dict) 
# {'apple': 100, 'list': [1, 2, 3]}
# 마지막 값을 기준으로 갱신된다. 
