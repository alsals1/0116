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