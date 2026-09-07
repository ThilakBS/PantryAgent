-- stores info about users
CREATE TABLE users (
    user_id     SERIAL PRIMARY KEY,
    user_name   text NOT NULL,
    contact     text NOT NULL,
    join_date   DATE NOT NULL DEFAULT CURRENT_DATE
);

-- creates virtual pantry to store food info
CREATE TYPE cate AS ENUM ('meat', 'veg', 'fruit', 'frozen', 'drinks', 'snacks', 'dry', 'mis');
CREATE TYPE u AS ENUM ('mL', 'L', 'g', 'kg', 'oz', 'lb', 'count');

CREATE TABLE pantry (
    obj_id      SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users(user_id),
    food_name   TEXT NOT NULL,
    quantity    FLOAT NOT NULL CHECK (quantity >= 0),
    unit        u NOT NULL,
    date_added  DATE NOT NULL DEFAULT CURRENT_DATE,
    expiration  DATE,
    category    cate NOT NULL
);

-- stores convos by session
CREATE TABLE convos (
    convo_id    SERIAL PRIMARY KEY,
    user_id     INTEGER NOT NULL REFERENCES users(user_id),
    ses_time    TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title       text
);

-- stores messages between the user and agent
CREATE TYPE roles AS ENUM ('user', 'assistant');

CREATE TABLE messages (
    mes_id      SERIAL PRIMARY KEY,
    convo_id    INTEGER NOT NULL REFERENCES convos(convo_id),
    mes_role    roles NOT NULL,
    content     text NOT NULL,
    convo_time  TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
