

DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_id_seq;
CREATE TABLE users (
    id serial NOT NULL,
    username varchar(20) UNIQUE,
    password varchar(20)
);

DROP TABLE IF EXISTS public.planet-votes;
DROP SEQUENCE IF EXISTS public.planet-votes_seq;
CREATE TABLE planet-votes (
    id serial NOT NULL,
    planet-id integer,
    planet_name varchar(30),
    user_id integer,
    submission_time timestamp without time zone
);


ALTER TABLE ONLY users
    ADD CONSTRAINT pk_users_id PRIMARY KEY (id);
ALTER TABLE ONLY planet-votes
    ADD CONSTRAINT pk_planet-votes_id PRIMARY KEY (id);
ALTER TABLE ONLY planet-votes
    ADD CONSTRAINT fk_user_id FOREIGN KEY user_id REFERENCES users(id);