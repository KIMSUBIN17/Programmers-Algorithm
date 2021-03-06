/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/62284 */

-- 코드를 입력하세요
SELECT cart_id
from cart_products
where name in ('Milk','Yogurt')
group by cart_id
having count(distinct name) = 2
order by cart_id



/*
ver.Oracle
where name in ('Milk','Yogurt')
--> 구입한 상품 중 Milk 또는 Yogurt 가 포함되어 있는 것만 

group by cart_id
--> cart_id 별로 그룹화

cart_id별로 그룹화한 데이터 상품 종류 중

*/
