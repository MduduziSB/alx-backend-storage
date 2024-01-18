-- The following script creates 'users' table if it doesn't exists
-- Attributes:
-- id (INT)
-- email (string)
-- name (string)
-- contry (enumeration)

CREATE TABLE IF NOT EXISTS users (
   id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
   email VARCHAR(255) NOT NULL UNIQUE,
   name VARCHAR(255),
   country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
