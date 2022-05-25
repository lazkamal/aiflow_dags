SELECT * FROM table;

-- templatised table name using Jinja
SELECT * FROM {{ params.dynamic_table }};
