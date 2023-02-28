CREATE TABLE project (
    name text PRIMARY KEY, 
    DESCRIPTION text, 
    deadline date
);

CREATE TABLE task (
    id integer PRIMARY KEY key AUTOINCREMENT NOT NULL, 
    priority integer default  1,
    details text,  
    status text, 
    deadline date, 
    completed_on date, 
    project text NOT NULL REFERENCES project(name)
)