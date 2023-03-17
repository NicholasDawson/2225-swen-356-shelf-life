DROP TABLE IF EXISTS shelf;
CREATE TABLE shelf (
  shelfId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  shelfName String DEFAULT 'Unnamed Shelf',
  userId UUID NOT NULL REFERENCES users (userId)
);