create table analytics.dim_asset (
	asset_id Integer generated always as identity primary key,-- internal unique id for the asset
	ticker varchar(20) not null unique, -- market ticker 
	asset_name varchar(100) not null, -- name
	asset_class varchar(30) not null, -- asset class e.g. - Equity, Crypto, Benchmark
	sector varchar(50), -- e.g. Technology, Financial, Healthcare
	currency varchar(10) not null, -- trading currency
	data_source varchar(50) not null, -- where the market data comes from
	is_active boolean not null default true, -- whether the asset is currently included
	created_at timestamp not null default current_timestamp -- when asset record was created
);

select * from analytics.dim_asset;

create table analytics.dim_date)(
	date_id integer primary key,
	full_date date not null unique,
	year smallint not null,
	quarter smallint not null,
	month smallint not null,
	month_name varchar(15) not null,
	week smallint not_null,
	day_of_month smallint not null,
	day_of_we
);
