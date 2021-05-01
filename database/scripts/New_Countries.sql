-- SEQUENCE: ctgov.countries_new_id_seq
CREATE SEQUENCE ctgov.countries_new_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctgov.countries_new_id_seq
	OWNER TO "postgres";
	
CREATE TABLE ctgov.countries_new
(
    id integer NOT NULL DEFAULT nextval('ctgov.countries_new_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default",
    display_order integer NOT NULL,
    CONSTRAINT countries_new_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE ctgov.countries_new
    OWNER to "postgres";

CREATE INDEX countries_new_order_idx
    ON ctgov.countries_new USING btree
    (display_order ASC NULLS LAST)
    TABLESPACE pg_default;

INSERT INTO ctgov.countries_new(name, display_order)
SELECT name, row_number() OVER (order by name) as display_order
FROM (SELECT DISTINCT name FROM ctgov.countries ORDER BY name ASC) AS foo;

UPDATE ctgov.countries_new SET display_order = 0 WHERE name = 'United States';

SELECT * FROM ctgov.countries_new ORDER BY display_order;