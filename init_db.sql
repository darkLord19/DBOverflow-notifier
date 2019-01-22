CREATE TABLE Persons (
    id tinyint AUTO_INCREMENT, 
    first_name varchar(255) NOT NULL,
    last_name varchar(255),
    PRIMARY KEY (ID)
);

CREATE TABLE Tasks (
    task_id smallint AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    PRIMARY KEY (TASK_ID)
);