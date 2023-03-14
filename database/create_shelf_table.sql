DROP TABLE IF EXISTS shelf;
CREATE TABLE shelf (
  shelfId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  userId UUID NOT NULL REFERENCES users (userId)
);