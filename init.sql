-- Create the users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    balance INTEGER DEFAULT 0
);

-- Create the transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    transaction_type TEXT NOT NULL,
    points INTEGER NOT NULL,
    transaction_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);