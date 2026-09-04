
CREATE TYPE cate AS ENUM ('meat', 'veg', 'fruit', 'frozen', 'drinks', 'snacks', 'dry', 'mis');
CREATE TYPE u AS ENUM ('mL', 'L', 'g', 'kg', 'oz', 'lb', 'count');

CREATE TABLE pantry (
    obj_id      SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL,
    name        TEXT NOT NULL,
    quantity    FLOAT NOT NULL CHECK (quantity >= 0),
    unit        u NOT NULL,
    date_added  DATE NOT NULL DEFAULT CURRENT_DATE,
    expiration  DATE,
    category    cate NOT NULL
);
