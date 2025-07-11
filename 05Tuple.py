'''
튜플(Tuple)
: 소괄호 () 안에 콤마로 구분된 항목들이 나열되어 표현되는 시퀀스 자료형.
  서로 다른 항목으로 구성할 수 있고, 인덱싱, 슬라이싱 등 기본적인 사용법은
  리스트와 동일하지만, 항목을 변경할 수 없는 Immutable 데이터 타입이다.
'''

# 함수를 통해 빈 튜플 생성
tu1 = tuple()
# 소괄호의 초기값을 통해 튜플 생성 및 초기화
tu2 = (1,2,3,4,5)
# 1개의 항목을 갖는 튜플생성. 뒤에 , 가 없으면 일반적인 변수 생성.
tu3 = 1,
tu4 = (98,99,100)
print(tu1, tu2, tu3)

print(f"{'인덱싱/슬라이싱':-^30}")
print('tu2[0]', tu2[0])
# 음수로 인덱스를 사용하면 마지막 항목부터 접근
print('tu2[-1]', tu2[-1]) # 5출력
print('tu2[1:3]', tu2[1:3]) # 마지막은 제외되므로 1~2까지 슬라이싱

# 튜플에 포함된 경우에는 True 반환
print(f"{'포함여부확인':-^30}")
print('4 in tu2', 4 in tu2)
print('99 not in tu2', 99 not in tu2)

print(f"{'반복출력':-^30}")
print('tu2 * 3',tu2 * 3)

# 튜플 병합 : 2개의 튜플을 하나로 합침
print(f"{'병합':-^30}")
new_tu = tu2 + tu4
print("new_tu", new_tu)

print(f"{'튜플과 리스트 변환':-^30}")
my_list = [1,2,3]
my_tuple = ('x', 'y', 'z')
print(tuple(my_list))
print(list(my_tuple))
