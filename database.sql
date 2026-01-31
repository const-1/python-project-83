-- Create urls table if not exists
CREATE TABLE IF NOT EXISTS urls (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create url_checks table for step 4
CREATE TABLE IF NOT EXISTS url_checks (
    id BIGSERIAL PRIMARY KEY,
    url_id BIGINT REFERENCES urls(id) ON DELETE CASCADE,
    status_code INTEGER,
    h1 VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add index for better performance
CREATE INDEX IF NOT EXISTS idx_url_checks_url_id ON url_checks(url_id);
