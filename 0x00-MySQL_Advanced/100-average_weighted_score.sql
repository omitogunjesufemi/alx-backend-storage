-- Procedure that computes and store the average weighted score for student

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;

    -- Calculate the total weighted score for the user
    SELECT SUM(corrections.score * projects.weight)
    INTO total_weighted_score
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate the total weight of the projects
    SELECT SUM(projects.weight)
    INTO total_weight
    FROM projects;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;
END //

DELIMITER ;
