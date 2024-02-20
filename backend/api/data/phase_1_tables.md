```sql
                                           Table "public.sp_500_companies"
        Column         |          Type          | Collation | Nullable |                   Default
-----------------------+------------------------+-----------+----------+----------------------------------------------
 id                    | integer                |           | not null | nextval('sp_500_companies_id_seq'::regclass)
 exchange              | character varying(255) |           | not null |
 symbol                | character varying(10)  |           | not null |
 short_name            | character varying(255) |           |          |
 long_name             | character varying(255) |           |          |
 sector                | character varying(255) |           |          |
 industry              | character varying(255) |           |          |
 current_price         | numeric(15,2)          |           |          |
 market_cap            | numeric(15,2)          |           |          |
 ebitda                | numeric(15,2)          |           |          |
 revenue_growth        | numeric(10,2)          |           |          |
 city                  | character varying(255) |           |          |
 state                 | character varying(255) |           |          |
 country               | character varying(255) |           |          |
 long_business_summary | text                   |           |          |
 weight                | numeric(10,2)          |           |          |
Indexes:
    "sp_500_companies_pkey" PRIMARY KEY, btree (id)

public_companies_test_db=# \d sp_500_companies, sp_500_index_levels, sp_500_stocks
Did not find any relation named "sp_500_companies,".
public_companies_test_db=# \d sp_500_index_levels
                                      Table "public.sp_500_index_levels"
   Column    |          Type          | Collation | Nullable |                     Default
-------------+------------------------+-----------+----------+-------------------------------------------------
 id          | integer                |           | not null | nextval('sp_500_index_levels_id_seq'::regclass)
 date        | date                   |           | not null |
 index_level | numeric(15,2)          |           |          |
 index_name  | character varying(255) |           | not null |
Indexes:
    "sp_500_index_levels_pkey" PRIMARY KEY, btree (id)

public_companies_test_db=# \d sp_500_stocks
                                     Table "public.sp_500_stocks"
  Column   |          Type          | Collation | Nullable |                  Default
-----------+------------------------+-----------+----------+-------------------------------------------
 id        | integer                |           | not null | nextval('sp_500_stocks_id_seq'::regclass)
 date      | date                   |           | not null |
 symbol    | character varying(10)  |           | not null |
 adj_close | numeric(15,2)          |           |          |
 close     | numeric(15,2)          |           |          |
 high      | numeric(15,2)          |           |          |
 low       | numeric(15,2)          |           |          |
 open      | numeric(15,2)          |           |          |
 volume    | character varying(255) |           |          |
Indexes:
    "sp_500_stocks_pkey" PRIMARY KEY, btree (id)
```