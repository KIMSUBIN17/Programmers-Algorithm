/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131533 */


SELECT P.PRODUCT_CODE, SUM(P.PRICE*O.SALES_AMOUNT) AS SALES
FROM PRODUCT P INNER JOIN OFFLINE_SALE O
ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE



'''
# 문제


# 풀이과정
1. 발생오류
ORA-00979: not a GROUP BY expression (GROUP  BY 표현식이 아닙니다)
P.PRICE*O.SALES_AMOUNT) AS SALES 를 SUM으로 묶지 않으면 GROUP BY에서 오류가 남
--> SELECT 에 있는 모든 컬럼명이나 표현식 중 집계함수를 제외하고는 모두 GROUP BY 절에 작성해야함 
2. 수정
- PRODUCT 테이블과 OFFLINE_SALE 테이블을 PRODUCT_ID 기준으로 조인
- PRODUCT 테이블의 PRICE, OFFLINE테이블의 SALES_AMOUNT의 곱을 SUM으로 묶음
--> 상품코드 별 매출액(판매가 * 판매량) 합계 = SUM(P.PRICE*O.SALES_AMOUNT)
- PRODUCT_CODE기준으로 그룹화




# 다른 풀이
1. JOIN 없이 풀기
SELECT P.PRODUCT_CODE, SUM(P.PRICE*O.SALES_AMOUNT) AS SALES
FROM PRODUCT P,OFFLINE_SALE O
WHERE P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE


'''
