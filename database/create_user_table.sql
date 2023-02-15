DROP TABLE IF EXISTS users;

CREATE TABLE users (
  userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username TEXT UNIQUE NOT NULL
);