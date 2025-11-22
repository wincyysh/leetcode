# Write your MySQL query statement below
SELECT project_id, round((sum(experience_years)/count(e.employee_id)),2) 
AS average_years 
FROM Project p Join Employee e ON p.employee_id = e.employee_id 
AND e.experience_years IS NOT NULL GROUP BY project_id 