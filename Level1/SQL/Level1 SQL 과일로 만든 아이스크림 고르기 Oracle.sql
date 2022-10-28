/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133025 */


SELECT F.FLAVOR
FROM FIRST_HALF F, ICECREAM_INFO I
WHERE F.FLAVOR = I.FLAVOR AND INGREDIENT_TYPE = 'fruit_based' 
AND TOTAL_ORDER >= 3000
ORDER BY TOTAL_ORDER DESC



