def solution(num1, num2):
    return int(num1/num2*1000)


''' 

# 람다식 사용ver
solution = lambda num1, num2 : int(num1/num2*1000)

기본 셋팅되던 지역변수 answer를 사용하지 않는 이유
-> 변수 저장을 위해서는 비용이 듦 
-> 시스템 성능의 저하가 올 수 있음
-> 재사용이 없는 함수 내 지역변수는 굳이 변수가 담지 않는 것을 추천함
  
  

'''
