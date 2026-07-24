CREATE TABLE Cultdetds (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    lol VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
 );

 INSERT INTO Cultdetds (name, lol) VALUES ('John Doe', 'Example');

SELECT * FROM Cultdetds;

DROP TABLE Cultdetds;