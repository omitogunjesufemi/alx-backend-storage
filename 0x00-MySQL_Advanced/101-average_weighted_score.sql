-- Procedure that computes and store the average weighted score for all student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;

    -- Declare cursor to iterate over users
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;

    -- Declare continue handler for the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET user_id = NULL;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        -- Fetch user_id from cursor
        FETCH user_cursor INTO user_id;
        
        -- Exit loop if no more users
        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the total weighted score for the user
        SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Calculate the total weight of all projects
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
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;
