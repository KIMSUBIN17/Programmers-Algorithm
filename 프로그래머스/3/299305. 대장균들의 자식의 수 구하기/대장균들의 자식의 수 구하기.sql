-- 코드를 작성해주세요
select parent.id, count(child.id) as child_count
from ECOLI_DATA  PARENT
left join ECOLI_DATA CHILD
on parent.id = child.parent_id
group by parent.id
order by parent.id