CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    certificate VARCHAR(512),
    file_path VARCHAR(512),
    created timestamp with time zone,
    modified timestamp with time zone
); 


CREATE TABLE IF NOT EXISTS content.genre (
   id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person (
   id uuid PRIMARY KEY,
   full_name VARCHAR(100),
   gender TEXT NOT NULL,
   created timestamp with time zone,
   modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
   id uuid PRIMARY KEY,
   genre_id uuid NOT NULL REFERENCES content.genre (id) ON DELETE CASCADE,
   film_work_id uuid NOT NULL REFERENCES content.film_work (id) ON DELETE CASCADE,
   created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
   id uuid PRIMARY KEY,
   role VARCHAR(100),
   created timestamp with time zone,
   person_id uuid NOT NULL REFERENCES content.person (id) ON DELETE CASCADE,
   film_work_id uuid NOT NULL REFERENCES content.film_work (id) ON DELETE CASCADE
);

ALTER ROLE app SET search_path TO content, public;

CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id, role);
CREATE UNIQUE INDEX film_work_genre_idx ON content.genre_film_work (film_work_id, genre_id);