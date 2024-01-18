-- SQL script that creates a trigger that resets the attribute valid_email

DELIMITER //
CREATE TRIGGER before_update_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being updated
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0; -- Reset valid_email to 0 when email changes
    END IF;
END;
//
DELIMITER ;
