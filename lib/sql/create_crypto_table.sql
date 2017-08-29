CREATE TABLE IF NOT EXISTS cryptos(
	source text NOT NULL,
    sub text NOT NULL,
	currency text NOT NULL,
	total_mentions integer,
    date_added timestamp
);
