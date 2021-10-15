/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12977 */


from itertools import combinations 

def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False
        return True
    
def solution(nums):
    answer = 0
    #순서고려하지 않고 r개의 데이터 뽑아 나열(조합)
    #nums에서 3개씩 고른 조합 list 만들기
    comb_nums = list(combinations(nums,3))

    #comb_nums에서 하나씩 가져와 sum값을 소수판별함
    for arr in comb_nums:
        #return 값이 True이면 count하기(=answer에 더하기)
        if is_prime(sum(arr)):
            answer += 1
    
    return answer

'''
#풀이
combination() 사용 : 맨 위에 from itertools import combinations  작성해야함
* itertools : 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
- permutations(순열-iterable객체에서 r개의 데이터 뽑아 일렬로 나열)
- combinations(조합 - iterable객체에서 r개의 데이터를 뽑아 순서 고려하지 않고 나열)

is_prime함수에서 for문 수행할 때 범위는 2~(num//2)+1로 설정

#다른 사람 풀이

from itertools import combinations
def prime_number(x):
    answer = 0
    #에라토스테네스의 체 사용->소수찾기
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])


--------------------
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
입출력 예 설명
입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.


'''