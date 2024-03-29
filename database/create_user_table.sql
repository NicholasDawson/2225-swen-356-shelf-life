ALTER TABLE shelf DROP CONSTRAINT IF EXISTS shelf_userid_fkey;

DROP TABLE IF EXISTS users; 
CREATE TABLE users (
  userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  google_id TEXT UNIQUE NOT NULL
);