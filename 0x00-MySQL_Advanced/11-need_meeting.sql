-- Create the view need_meeting

CREATE VIEW need_meeting AS
SELECT
    student_id,
    student_name
FROM
    students
WHERE
    score < 80
    AND (students.last_meeting IS NULL OR DATEDIFF(NOW(), students.last_meeting) > 30);

