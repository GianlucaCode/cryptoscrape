CREATE TABLE IF NOT EXISTS reddit_comments(
	sub nvarchar NOT NULL,
	currency nvarchar NOT NULL,
	post_id nvarchar NOT NULL,
	contents nvarchar NOT NULL,
	sentiment decimal,
	subjectivity decimal
);
