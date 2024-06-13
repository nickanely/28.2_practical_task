CREATE TABLE contacts (
    name VARCHAR(50),
    surname VARCHAR(50),
    phone VARCHAR(15)
);

CREATE OR REPLACE FUNCTION populate_contacts() RETURNS void AS $$
BEGIN
    INSERT INTO contacts (name, surname, phone) VALUES
    ('John', 'Doe', '123-456-7890'),
    ('Jane', 'Smith', '234-567-8901'),
    ('Alice', 'Johnson', '345-678-9012');
END;
$$ LANGUAGE plpgsql;
