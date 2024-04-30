-- Creates an index idx_name_first on the table and the furst
-- letter of name and the score
CREATE INDEX idx_name_first ON names (name(1), score);
