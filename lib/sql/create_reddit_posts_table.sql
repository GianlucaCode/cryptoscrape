CREATE TABLE IF NOT EXISTS reddit_posts(
	title text NOT NULL,
	sub text NOT NULL,
	currency text NOT NULL,
	contents text NOT NULL,
	sentiment decimal,
	subjectivity decimal
);
