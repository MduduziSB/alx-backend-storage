-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT
            IFNULL(SUM(corrections.score * projects.weight) / NULLIF(SUM(projects.weight), 0), 0)
        FROM corrections
        INNER JOIN projects ON projects.id = corrections.project_id
        WHERE corrections.user_id = p_user_id
    )
    WHERE id = p_user_id;
END $$
DELIMITER ;
