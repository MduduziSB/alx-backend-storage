-- Create the stored procedure ComputeAverageScoreForUser

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update or insert the average score for the user
    INSERT INTO average_scores (user_id, avg_score)
    VALUES (p_user_id, avg_score)
    ON DUPLICATE KEY UPDATE avg_score = avg_score;
END;
//
DELIMITER ;
