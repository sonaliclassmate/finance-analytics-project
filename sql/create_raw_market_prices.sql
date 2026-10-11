create table if not exists raw.market_prices(
	ticker varchar(20) not null,
	trading_date date not null,
	open_price numeric(18, 6),
	high_price numeric(18, 6),
	low_price numeric(18,6),
	close_price numeric(18,6),
	adjusted_close numeric(18,6),
	volume bigint,
	dividents numeric(18,6),
	stock_splits numeric(18,6),
	data_source varchar(50) not null default 'Yahoo Finance',
	loaded_at timestamptz not null default current_timestamp,

	constraint pk_market_prices
		primary key (ticker, trading_date),

	constraint fk_market_prices_asset
		foreign key (ticker)
		references analytics.dim_asset(ticker)
	
);

