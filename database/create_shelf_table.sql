DROP TABLE IF EXISTS shelf;
CREATE TABLE shelf (
  shelfId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  userId UUID REFERENCES users (userId) NOT NULL
);