
# Question_4

Creating a simple website which allow users
to register or login.when user clicks on login,he should enter his credentials and validating it with existing UserID, Password. If successful,a new webpage pops out and displays, “Welcome To IIT Indore” with college logo.





## Installation

1.Clone the repository 

```bash
git clone https://github.com/VIKAS-047/a7_question_4.git
```

```bash
cd a7_question_4
```
2.Install Required Python Libraries

```bash
pip install Flask
```

```bash
pip install mysql-connector-python
```

3.Setting Up MySQL Database

```bask
CREATE DATABASE user_data;

USE user_data;

CREATE TABLE user_space (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

4.Update Database Credentials

```bash
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="user_data"
)
```


## Running Tests

To run tests, run the following command

```bash
  python app.py
```


## Screenshots

![Screenshot (127)](https://github.com/user-attachments/assets/2ddb84ce-0205-40c6-a315-93102142de5b)

![Screenshot (128)](https://github.com/user-attachments/assets/b435c0c7-1baa-4e15-a7f7-20acecd005fd)

![Screenshot (129)](https://github.com/user-attachments/assets/4dd2812c-c693-4c03-b117-2e38b153e89a)




