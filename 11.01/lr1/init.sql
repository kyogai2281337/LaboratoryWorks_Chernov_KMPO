CREATE DATABASE IF NOT EXISTS university;

CREATE TABLE caphedras (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  maintainer VARCHAR(255),
  room INT,
  corp INT,
  phone VARCHAR(20),
  teachers_count INT,
);


CREATE TABLE faculcies (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  dekan VARCHAR(255),
  caph_id INT
  room INT,
  corp INT,
  phone VARCHAR(20),
  FOREIGN KEY (caph_id) REFERENCES caphedras(id)
);

CREATE TABLE groups (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  invite_year INT,
  part INT,
  students_amount INT
);

CREATE TABLE students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  surname VARCHAR(255),
  name VARCHAR(255),
  sec_name VARCHAR(255),
  group_id INT,
  birth_year INT,
  gender VARCHAR(10),
  addr VARCHAR(255),
  town VARCHAR(255),
  phone VARCHAR(20),
  FOREIGN KEY (group_id) REFERENCES groups(id)
);

CREATE TABLE marks (
  id INT PRIMARY KEY AUTO_INCREMENT,
  group_id INT,
  student_id INT,
  sub VARCHAR(255),
  mark_date VARCHAR(64),
  mark INT,
  FOREIGN KEY (group_id) REFERENCES groups(id),
  FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE INDEX idx_group_name ON groups(name);
CREATE INDEX idx_student_name ON students(name);
CREATE INDEX idx_sub_name ON marks(sub);