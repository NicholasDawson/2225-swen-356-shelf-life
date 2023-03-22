DROP TABLE IF EXISTS food;
CREATE TABLE food (
  foodId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  shelfId UUID REFERENCES shelf (shelfId),
  foodName TEXT NOT NULL UNIQUE,
  expiration DATE,
  dateAdded DATE NOT NULL DEFAULT NOW(),
  quantity INT DEFAULT 1
);