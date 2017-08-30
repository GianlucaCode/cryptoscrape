CREATE TABLE IF NOT EXISTS reddit_comments(
	sub text NOT NULL,
	currency text NOT NULL,
	post_id text NOT NULL,
	contents text NOT NULL,
	sentiment decimal,
	subjectivity decimal
);
