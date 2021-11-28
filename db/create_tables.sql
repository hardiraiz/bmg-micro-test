CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS app_user (
    username varchar(30) NOT NULL UNIQUE,
    name varchar(35) NOT NULL,
    email varchar(45) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    refferal_code varchar(45) NOT NULL UNIQUE,
    id uuid NOT NULL,
    PRIMARY KEY (id)
);