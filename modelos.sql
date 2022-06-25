CREATE TABLE person (
  person_id INTEGER UNSIGNED  NOT NULL  ,
  name VARCHAR(100)  NOT NULL  ,
  second_name VARCHAR(100)  NULL  ,
  lastname VARCHAR(100)  NOT NULL  ,
  second_lastname VARCHAR(100)  NULL  ,
  age INTEGER UNSIGNED  NOT NULL    ,
PRIMARY KEY(person_id));



CREATE TABLE doctor (
  doctor_id INTEGER UNSIGNED  NOT NULL  ,
  person_id INTEGER UNSIGNED  NOT NULL  ,
  title VARCHAR(100)  NULL    ,
PRIMARY KEY(doctor_id)  ,
INDEX doctor_FKIndex1(person_id),
  FOREIGN KEY(person_id)
    REFERENCES person(person_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);



CREATE TABLE doctor_acount (
  doctor_account_id INTEGER UNSIGNED  NOT NULL  ,
  doctor_id INTEGER UNSIGNED  NOT NULL  ,
  doctor_username VARCHAR(100)  NULL  ,
  doctor_email VARCHAR(100)  NULL  ,
  doctor_password VARCHAR(100)  NULL    ,
PRIMARY KEY(doctor_account_id)  ,
INDEX doctor_acount_FKIndex1(doctor_id),
  FOREIGN KEY(doctor_id)
    REFERENCES doctor(doctor_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);



CREATE TABLE patient (
  patient_id INTEGER UNSIGNED  NOT NULL  ,
  person_id INTEGER UNSIGNED  NOT NULL    ,
PRIMARY KEY(patient_id)  ,
INDEX patient_FKIndex1(person_id),
  FOREIGN KEY(person_id)
    REFERENCES person(person_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);



CREATE TABLE patient_diagnostic (
  diagnostic_id INTEGER UNSIGNED  NOT NULL  ,
  doctor_id INTEGER UNSIGNED  NOT NULL  ,
  patient_id INTEGER UNSIGNED  NOT NULL  ,
  diagnostic_text TEXT  NOT NULL    ,
PRIMARY KEY(diagnostic_id, doctor_id)  ,
INDEX patient_diagnostic_FKIndex1(patient_id)  ,
INDEX patient_diagnostic_FKIndex2(doctor_id),
  FOREIGN KEY(patient_id)
    REFERENCES patient(patient_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE,
  FOREIGN KEY(doctor_id)
    REFERENCES doctor(doctor_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);



CREATE TABLE phone_numbers (
  phone_number VARCHAR(10)  NOT NULL  ,
  patient_id INTEGER UNSIGNED  NOT NULL    ,
PRIMARY KEY(phone_number)  ,
INDEX phone_numbers_FKIndex1(patient_id),
  FOREIGN KEY(patient_id)
    REFERENCES patient(patient_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);



CREATE TABLE user_account (
  user_account_id INTEGER UNSIGNED  NOT NULL  ,
  patient_id INTEGER UNSIGNED  NOT NULL  ,
  user_email VARCHAR(100)  NOT NULL  ,
  user_password VARCHAR(100)  NOT NULL  ,
  username VARCHAR(100)  NOT NULL    ,
PRIMARY KEY(user_account_id)  ,
INDEX user_account_FKIndex1(patient_id),
  FOREIGN KEY(patient_id)
    REFERENCES patient(patient_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);



CREATE TABLE vital_signs (
  register_number INTEGER UNSIGNED  NOT NULL  ,
  patient_id INTEGER UNSIGNED  NOT NULL  ,
  oxigen INTEGER UNSIGNED  NOT NULL  ,
  heart_rate INTEGER UNSIGNED  NOT NULL  ,
  temperature FLOAT  NULL  ,
  resp_rate INTEGER UNSIGNED  NULL  ,
  weight INTEGER UNSIGNED  NULL  ,
  height INTEGER UNSIGNED  NULL  ,
  day_taken INTEGER UNSIGNED  NULL  ,
  year_taken INTEGER UNSIGNED  NULL  ,
  month_taken INTEGER UNSIGNED  NULL  ,
  hour_taken INTEGER UNSIGNED  NULL    ,
PRIMARY KEY(register_number)  ,
INDEX vital_signs_FKIndex1(patient_id),
  FOREIGN KEY(patient_id)
    REFERENCES patient(patient_id)
      ON DELETE RESTRICT
      ON UPDATE CASCADE);




