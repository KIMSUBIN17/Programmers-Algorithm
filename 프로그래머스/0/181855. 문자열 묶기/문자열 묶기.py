def solution(strArr):
    tmp = []    #각 길이별 문자열의 갯수를 저장할 빈 리스트 선언
    #문자열 배열 strArr에 대해 각 문자열의 길이 계산해 리스트에 저장
    answer = [len(i) for i in strArr]
    #중복제거해 리스트에 있는 고유한 길이들을 순회함
    for i in set(answer):
    #각 고유한 길이 i에 대해 해당 길이가 answer 리스트에 몇번 등장하는지 세어 tmp에 추가(각 길이별로 몇 개의 문자열이 있는지 tmp리스트에 저장)
        tmp.append(answer.count(i))
    #리스트에서 가장 큰 값 반환(=가장 많은 개수를 가진 길이)
    return max(tmp)


'''
#오답노트 
Q. 중복제거를 꼭 해야하는가?
A. 문제에서는 문자열의 길이가 같은 것끼리 그룹을 만들어 그룹의 개수 중 가장 많은 그룹의 크기를 반환하게 되어있음
--> 각 그룹에 속하는 문자열들의 길이를 기준으로 그룹 만들어야함
중복 제거를 하지 않고 문자열의 길이를 직접 비교하면, 
EX)"abc"와 "def"가 있을 때, "abc"의 길이와 "def"의 길이를 비교하여 그룹을 만든다면
이 경우에는 "abc"와 "def"가 서로 다른 그룹으로 분류되어야 함

문제에서는 길이가 같은 문자열들끼리 그룹을 만들어야하므로, 중복된 길이를 하나의 그룹으로 묶어줘야함
=> 중복제거가 필요한 이유(☆)
=> 중복제거를 통해 각 길이별로 하나의 그룹을 만들어주고, 그룹별로 문자열의 개수를 세어서 max를 구해야함

'''
