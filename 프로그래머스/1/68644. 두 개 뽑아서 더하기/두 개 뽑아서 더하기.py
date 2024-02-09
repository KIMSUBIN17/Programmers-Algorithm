def solution(numbers):
    answer = []
    #이중for문 -->  모든 가능한 조합 찾기위함
    # numbers리스트의 모든 요소 하나씩순회
    for i in range(len(numbers)):
        #첫번째 반복문에서 선택된 요소 이후의 요소들과의 조합 찾음
        #서로 다른 인덱스에 있는 두 개의 수를 선택
        for j in range(i+1, len(numbers)):
            #두 수의 합을 리스트에 추가
            answer.append(numbers[i] + numbers[j])
    #set()사용해서 중복제거
    answer=list(set(answer))
    #리스트 오름차순 정렬
    answer.sort()
    return answer



'''
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer
    
    
from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)   
>> combinations(numbers,2)는 리스트안에 2개의 요소로 구할 수 있는 모든 조합을 반환

    
다른풀이_pythonic 풀이
두개이상의 리스트에서 조합을 리턴
from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,
'''