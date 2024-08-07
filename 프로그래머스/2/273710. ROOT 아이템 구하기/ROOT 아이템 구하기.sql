-- 코드를 작성해주세요
SELECT I.ITEM_ID, I.ITEM_NAME
FROM ITEM_INFO I JOIN ITEM_TREE T
ON I.ITEM_ID = T.ITEM_ID
WHERE ISNULL(T.PARENT_ITEM_ID)

/*
ISNULL(MYSQL) -- oracle의 NVL함수 역할
NVL 또는 ISNULL(a,b) : a의 결과값이 null이면 b출력
*/