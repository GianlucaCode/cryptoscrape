CREATE TABLE IF NOT EXISTS cryptos(
	source text NOT NULL,
	name text NOT NULL,
	total_mentions integer,
    date_added timestamp
);
