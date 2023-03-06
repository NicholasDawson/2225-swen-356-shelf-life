ALTER TABLE shelf DROP CONSTRAINT IF EXISTS shelf_userid_fkey;
ALTER TABLE shelf DROP CONSTRAINT IF EXISTS shelf_foodid_fkey;

DROP TABLE IF EXISTS users; 
CREATE TABLE users (
  userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username TEXT UNIQUE NOT NULL
);