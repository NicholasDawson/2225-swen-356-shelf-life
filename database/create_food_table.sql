DROP TABLE IF EXISTS food;
CREATE TABLE food (
  foodId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL UNIQUE,
  expiration DATE,
  dateAdded DATE NOT NULL,
  quantity INT DEFAULT 1
);