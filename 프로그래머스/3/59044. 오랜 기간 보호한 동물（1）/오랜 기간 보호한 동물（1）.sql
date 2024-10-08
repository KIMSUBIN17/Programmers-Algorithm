-- 코드를 입력하세요
SELECT * 
FROM (
    SELECT A.NAME, A.DATETIME
    FROM ANIMAL_INS A LEFT OUTER JOIN ANIMAL_OUTS B
    ON A.ANIMAL_ID = B.ANIMAL_ID
    WHERE B.ANIMAL_ID IS NULL
    ORDER BY A.DATETIME
)
WHERE ROWNUM < 4

/*
INS -> A 보호시작일 (JOIN기준) 이름, 보호시작일
OUTS -> B 입양일
ROWNUM < 4 (3까지)
*/