-- Creates a function that divides (and returns float)
-- the first by the second or return 0 if second number = 0
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	DECLARE results FLOAT;

	IF b = 0 THEN
	SET results = 0;
	ELSE
	SET results = a/b;
	END IF;

	RETURN results;
END//

DELIMITER ;
