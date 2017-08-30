CREATE TABLE IF NOT EXISTS reddit_posts(
	sub text NOT NULL,
	contents text NOT NULL,
	sentiment decimal,
	subjectivity decimal
);
