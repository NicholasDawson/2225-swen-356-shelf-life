DROP TABLE IF EXISTS "user";

CREATE TABLE "user" (
  userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username TEXT UNIQUE NOT NULL
);