-- 코드를 작성해주세요
SELECT ID, LENGTH
FROM FISH_INFO
# 10cm 미만이면 null이므로 LENGTH가 NULL이면 10으로 지정
ORDER BY IFNULL(LENGTH,10) DESC, ID
LIMIT 10
