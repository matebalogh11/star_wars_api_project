ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planetvotes DROP CONSTRAINT IF EXISTS pk_planetvotes_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.planetvotes DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;



DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_id_seq;
CREATE TABLE users (
    id serial NOT NULL,
    username varchar(20) UNIQUE,
    password varchar(100)
);

DROP TABLE IF EXISTS public.planetvotes;
DROP SEQUENCE IF EXISTS public.planetvotes_seq;
CREATE TABLE planetvotes (
    id serial NOT NULL,
    planet_id integer,
    planet_name varchar(30),
    user_id integer,
    submission_time timestamp without time zone
);


ALTER TABLE ONLY users
    ADD CONSTRAINT pk_users_id PRIMARY KEY (id);
ALTER TABLE ONLY planetvotes
    ADD CONSTRAINT pk_planetvotes_id PRIMARY KEY (id);
ALTER TABLE ONLY planetvotes
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);
