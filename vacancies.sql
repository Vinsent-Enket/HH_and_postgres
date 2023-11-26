DROP TABLE IF EXISTS vacancies CASCADE;
CREATE TABLE vacancies (id INTEGER PRIMARY KEY,
name VARCHAR(50),
area VARCHAR(30),
salary INTEGER,
published_at DATE,
employer_id INTEGER, -- связать с таблицей employer
requirement VARCHAR(100),
employment VARCHAR(100),
url VARCHAR(50));
