DROP TABLE IF EXISTS food;

CREATE TABLE food (
  foodId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  shelfId UUID REFERENCES shelf (shelfId) NOT NULL,
  name TEXT NOT NULL UNIQUE,
  expiration DATE,
  dateAdded TIMESTAMP NOT NULL DEFAULT NOW()
);