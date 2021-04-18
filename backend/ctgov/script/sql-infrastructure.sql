-- SEQUENCE: ctfrontier.race_id_seq
CREATE SEQUENCE ctgov.race_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctgov.race_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.route_of_administration_id_seq
CREATE SEQUENCE ctgov.route_of_administration_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
	
ALTER SEQUENCE ctgov.route_of_administration_id_seq
	OWNER TO "postgres";
	
-- TABLE: ctgov.study_race
CREATE TABLE ctgov.race
(
	id integer NOT NULL DEFAULT nextval('ctgov.race_id_seq'::regclass),
	race text,
	nct_id text NOT NULL,
	CONSTRAINT race_pkey PRIMARY KEY(id),
	CONSTRAINT race_nct_id_fkey FOREIGN KEY (nct_id)
        REFERENCES ctgov.studies (nct_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;
	
-- TABLE: ctgov.study_roa
CREATE TABLE ctgov.route_of_administration
(
	id integer NOT NULL DEFAULT nextval('ctgov.route_of_administration_id_seq'::regclass),
	roa text,
	nct_id text NOT NULL,
	CONSTRAINT roa_pkey PRIMARY KEY(id),
	CONSTRAINT roa_nct_id_fkey FOREIGN KEY (nct_id)
        REFERENCES ctgov.studies (nct_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;