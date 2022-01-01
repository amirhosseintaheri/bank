CREATE TABLE Bank

( Code           VARCHAR(255)   NOT NULL,

  Bank_Name      VARCHAR(30) NOT NULL,

  Addr           VARCHAR(255)      NOT NULL,

  Bank_Code       INT   NOT NULL,

  Branch_no      INT NOT NULL,

PRIMARY KEY   (Code));



CREATE TABLE Branch

( Addr           VARCHAR(255)   NOT NULL,

  Branch_no      INT NOT NULL,

  Bank_Code      VARCHAR(255)      NOT NULL,

PRIMARY KEY   (Branch_no,Bank_Code),

FOREIGN KEY (Bank_code) REFERENCES Bank(Code));



CREATE TABLE Account

( Acct_no           VARCHAR(255)   NOT NULL,

  Balance           INT    NOT NULL,

  Acct_Type           BINARY(2)      NOT NULL,

  Bank_Code           VARCHAR(255)   NOT NULL,

  Branch_no      INT NOT NULL,

PRIMARY KEY   (Acct_no),

FOREIGN KEY (Branch_no,Bank_Code) REFERENCES Branch(Branch_no,Bank_Code));



CREATE TABLE Loan

( Loan_no           VARCHAR(255)   NOT NULL,

  Amount           INT    NOT NULL,

  Loan_Type           BINARY(2)      NOT NULL,

  Bank_Code           VARCHAR(255)   NOT NULL,

  Branch_no      INT NOT NULL,

PRIMARY KEY   (Loan_no),

FOREIGN KEY (Branch_no,Bank_Code) REFERENCES Branch(Branch_no,Bank_Code));



CREATE TABLE Customer

( Ssn           INT  NOT NULL,

  Customer_Name           VARCHAR(255)    NOT NULL,

  Addr           VARCHAR(255)      NOT NULL,

  Phone           INT      NOT NULL,

PRIMARY KEY   (Ssn),

UNIQUE      (Phone));



CREATE TABLE Account_Customer

( Ssn           INT  NOT NULL,

  Account_no           VARCHAR(255)   NOT NULL,

FOREIGN KEY (ssn) REFERENCES Customer(Ssn),

FOREIGN KEY (Account_no) REFERENCES Account(Acct_no));



CREATE TABLE Loan_Customer

( Ssn           INT  NOT NULL,

  Loan_no           VARCHAR(255)   NOT NULL,

FOREIGN KEY (Ssn) REFERENCES Customer(Ssn),

FOREIGN KEY (Loan_no) REFERENCES Loan(Loan_no));