CREATE TABLE project (
    name text PRIMARY KEY, 
    DESCRIPTION text, 
    deadline date
);

CREATE TABLE task (
    id integer PRIMARY KEY key AUTOINCREMENT NOT NULL, 
    priority text, 
    status text, 
    deadline date, 
    completed_on date, 
    project text NOT NULL REFERENCES project(NAME)
)