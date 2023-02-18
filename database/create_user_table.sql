ALTER TABLE food DROP COLUMN IF EXISTS shelfId;
ALTER TABLE shelf DROP COLUMN IF EXISTS userId;
DROP TABLE IF EXISTS users; 
CREATE TABLE users (
  userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username TEXT UNIQUE NOT NULL,
  password TEXT UNIQUE NOT NULL
);