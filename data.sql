BEGIN;
--
-- Create model Course
--
CREATE TABLE "flashcard_app_course" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "section_num" integer NOT NULL, "semester" varchar(6) NOT NULL, "year" integer NOT NULL, "author_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model School
--
CREATE TABLE "flashcard_app_school" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
--
-- Create model FlashcardDeck
--
CREATE TABLE "flashcard_app_flashcarddeck" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "description" text NOT NULL, "author_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "course_id" bigint NULL REFERENCES "flashcard_app_course" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Flashcard
--
CREATE TABLE "flashcard_app_flashcard" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "front" text NOT NULL, "back" text NOT NULL, "flashcard_deck_id" bigint NOT NULL REFERENCES "flashcard_app_flashcarddeck" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "flashcard_app_course_author_id_2f0b7933" ON "flashcard_app_course" ("author_id");
CREATE INDEX "flashcard_app_flashcarddeck_author_id_550703a1" ON "flashcard_app_flashcarddeck" ("author_id");
CREATE INDEX "flashcard_app_flashcarddeck_course_id_7f5e4c2d" ON "flashcard_app_flashcarddeck" ("course_id");
CREATE INDEX "flashcard_app_flashcard_flashcard_deck_id_f7d88649" ON "flashcard_app_flashcard" ("flashcard_deck_id");
COMMIT;
