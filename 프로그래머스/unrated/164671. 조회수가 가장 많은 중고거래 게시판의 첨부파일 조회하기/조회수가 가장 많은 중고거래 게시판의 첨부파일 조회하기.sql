-- 코드를 입력하세요
SELECT '/home/grep/src/' || F.BOARD_ID || '/' || F.FILE_ID || F.FILE_NAME || F.FILE_EXT AS FILE_PATH
FROM USED_GOODS_FILE F
INNER JOIN USED_GOODS_BOARD B
ON F.BOARD_ID = B.BOARD_ID
WHERE VIEWS IN (SELECT MAX(VIEWS)
               FROM USED_GOODS_BOARD)
ORDER BY F.FILE_ID DESC