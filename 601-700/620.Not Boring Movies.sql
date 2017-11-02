select id,movie,description,rating
from cinema
where id%2=1 and description!="boring"
order by rating DESC
#DESC表示降序