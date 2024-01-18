-- Create a trigger that decreases the quantity of an item after adding a new order

DELIMITER //
CREATE TRIGGER after_insert_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE updated_quantity INT;

    -- Calculate the updated quantity by decrementing the item quantity
    SET updated_quantity = (SELECT quantity FROM items WHERE item_id = NEW.item_id) - 1;

    -- Update the item quantity in the items table
    UPDATE items SET quantity = updated_quantity WHERE item_id = NEW.item_id;
END;
//
DELIMITER ;

