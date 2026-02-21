SELECT candidate_id --, count(skill) as counter --> optional
FROM candidates
WHERE skill IN ('Python','Tableau','PostgreSQL') -- it's like --> WHERE skill = 'Python' OR skill = 'Tableau' OR skill = 'PostgreSQL'
GROUP BY candidate_id
HAVING count(skill) >= 3;

-- Things learned:
-- + can use group by without selecting aggregates
-- + can use having withough selecting aggregates( but applies on aggreated function )
-- + HAVING is mostly applied on aggreagated functions, but can also be used instead of WHERE (though it's weird!! :> )
