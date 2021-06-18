CREATE DATABASE dodocode;

CREATE TABLE page
(
    id              SERIAL PRIMARY KEY NOT NULL UNIQUE,
    metatitle       VARCHAR(70),
    metadescription VARCHAR(120),
    title           VARCHAR(70)        NOT NULL UNIQUE,
    body            TEXT,
    created         TIMESTAMP,
    updated         TIMESTAMP
);


CREATE TABLE redirect
(
    id      SERIAL PRIMARY KEY NOT NULL UNIQUE,
    page_id INTEGER DEFAULT NULL,
    path    VARCHAR(300) UNIQUE,
    changed TIMESTAMP,
    FOREIGN KEY (page_id) REFERENCES page (id)
);


CREATE TABLE storage
(
    id      SERIAL PRIMARY KEY NOT NULL UNIQUE,
    name    VARCHAR(64)        NOT NULL,
    path    VARCHAR(128) UNIQUE,
    type    VARCHAR(50),
    created TIMESTAMP
);
DROP TABLE "user";
CREATE TABLE "user"
(
    id       SERIAL PRIMARY KEY NOT NULL UNIQUE,
    name     VARCHAR(50),
    email    VARCHAR(80) UNIQUE,
    password VARCHAR(120)
)
-- SET session_replication_role = 'replica';
-- INSERT INTO redirect
-- VALUES (1, 1, 0, null, null);
-- SET session_replication_role = 'origin';