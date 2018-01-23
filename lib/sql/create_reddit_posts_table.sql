CREATE TABLE IF NOT EXISTS reddit_posts(
	title nvarchar NOT NULL,
	sub nvarchar NOT NULL,
	currency nvarchar NOT NULL,
	contents nvarchar NOT NULL,
	sentiment decimal,
	subjectivity decimal
);
