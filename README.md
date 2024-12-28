# Task Management API Documentation

## Overview

The **Task Management - API Project** provides a detailed guide to the API endpoints available in the Task Management project. The project includes functionalities for managing projects, tasks, and comments. Each section describes how to use the API for creating, retrieving, updating, and deleting resources.

---


<br>

## Technology Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL (with Supabase deployment)

---

<br>


## Instructions to Run Locally

### Prerequisites

- Python 3.12.2
- Django 4.2.4
- Django REST Framework 3.15.2
- PostgreSQL

### Packages used:

```bash
asgiref==3.8.1
Django==5.1.4
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
PyJWT==2.10.1
sqlparse==0.5.3
tzdata==2024.2
```

---

<br>

### Installation Steps

1. Open `command prompt` in the folder directory where you want to create & run the project locally

2. Copy the `repository_url` to **Clone the repository**

   ```bash
   git clone https://github.com/sayed8901/Task_Management_API_project.git
   cd Task_Management_API_project
   ```

3. **Create a virtual environment**

   ```bash
   python -m venv task_mgt_venv
   cd task_mgt_venv
   Scripts\activate.bat
   cd ..
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   code .
   ```

<br>

5. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Creating superuser**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

<br>

8. **Finally, Access the application**

- Local: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/login/

---

<br>



### Admin Panel Access

The Django Rest Framework Admin Panel can be accessed using the following credentials:

- **Username**: `sayed`  
- **Password**: `sayed8901`  


- **Admin Login**:  
  `POST` - `/admin/login/`  
  Allows the admin to log in.

---


## General Information

- All API endpoints require a **JWT access token** to be included in the request headers for authentication.
- Authorization Header Format:
  ```
  Authorization: Bearer <token>
  ```

---


## API Endpoints

### Postman Documentation
You can view and test the API endpoints using Postman. Access the API documentation here:

**Postman Documentation Link:** `https://documenter.getpostman.com/view/27420783/2sAYJ6CzUk`


### Base URL
**`http://127.0.0.1:8000`**


### Authentication


- **User Register**:  
  `POST` - `api/users/register/`  
  can register a new user by providing the following JSON input data. While creating an user, you can also set his/ her role (user_type) too.

  ```json
  {
    "username": "tasmi",
    "first_name": "Tasmiya",
    "last_name": "Akter",
    "email": "sdssayed24@gmail.com",
    "password": "sayed8901",
    "confirm_password": "sayed8901",
    "user_type": "member"
  }
  ```

- **User Login**:  
  `POST` - `/api/users/login/`  
  Authenticates any user and generates a session token and also can login.

  ```json
  {
    "username": "sayed",
    "password": "sayed8901",
  }
  ```

  - **User Logout**:  
  `POST` - `/api/users/logout/`  
  Any user can logout currently loggedin user by hitting the logout API endpoint.
  Note: You need to add "JWT access token" in the bearer token header field.


- **Get All Users**:  
  `GET` - `/api/users/`  
  This API will retrive all the existing users data list available in the database. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.


- **Get a single user**:  
  `GET` - `/api/users/<user_id>/`  
  Based on user_id, this API will retrive an individual users info from the database. This API is accessible to both "Admin" and "member" users.
  Note: Need to add "JWT access token" in the bearer token header field.


- **User Update**:  
  `PATCH` - `/api/users/<user_id>/`  
  Only "Admin user" can modify the info of an individual user by user_id. Even, while updating an user info, he can also update his/ her role too.
  Note: Need to add "JWT access token" in the bearer token header field.

  ```json
  {
    "first_name": "Miss Tasmia",
    "last_name": "Akter",
    "user_type": "member"
  }

- **Delete a single user**:  
  `DELETE` - `/api/users/<user_id>/`  
  Only "Admin user" can delete an individual user info from the database by user_id.
  Note: Need to add "JWT access token" in the bearer token header field.



## Project Management

### **Create a Project**

  `POST` - `http://127.0.0.1:8000/api/projects/`
  only "Admin user" can create a new project information.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
    "name": "Task Management Application",
    "description": "To manage the tasks, need to build an application using django rest framework.",
    "owner": 1
  }
  ```

---

### **Get All Projects**

  `GET` -  `http://127.0.0.1:8000/api/projects/`
  This API will retrive all the existing projects data list available in the database. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.


---

### **Get a Single Project**

  `GET` -  `http://127.0.0.1:8000/api/projects/<project_id>/`
  Based on project_id, this API will retrive an individual project info from the database. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.


---

### **Fully Modify a Project**

  `PUT` -  `http://127.0.0.1:8000/api/projects/<project_id>/`
  Only "Admin users" can fully modify all the field of the an individual project info by project_id.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
      "name": "Updated Project Name",
      "description": "Updated Project Description",
      "owner": 1
  }
  ```

---

### **Partially Update a Project**

  `PATCH` -  `http://127.0.0.1:8000/api/projects/<project_id>/`
  only "Admin user" can modify some part of the an individual project info by project_id.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
      "name": "Updated Project Name"
  }
  ```

---

### **Delete a Project**

  `DELETE` -  `http://127.0.0.1:8000/api/projects/<project_id>/`
Using this API, only "Admin user" can delete an individual project info from the database by project_id.
Note: You need to add "JWT access token" in the bearer token header field.

---


## Task Management

### **Create a Task**

  `POST` -  `http://127.0.0.1:8000/api/tasks/`
  you can create a new task information. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
      "title": "Task Title",
      "description": "Task Description",
      "status": "to do",
      "priority": "high",
      "created_at": "2024-12-28T14:33:09.477201Z",
      "due_date": "2024-12-28T14:33:06Z",
      "assigned_to": 2,
      "project": 2
  }
  ```

---

### **Get All Tasks**

  `GET` -  `http://127.0.0.1:8000/api/tasks/`
  This API will retrive all the existing tasks data list available in the database. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

---

### **Get a Single Task**

  `GET` - `http://127.0.0.1:8000/api/tasks/<task_id>/`
  Based on task_id, this API will retrive an individual task info from the database. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

---

### **Fully Modify a Task**

  `PUT` - `http://127.0.0.1:8000/api/tasks/<task_id>/`
  Using this API, only "Admin users" can fully modify all the field of the an individual task info by task_id. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
    "title": "User Authentication",
    "description": "Have to implement JWT token based authentication system for the user registration , login and logout.",
    "status": "in progress",
    "priority": "medium",
    "created_at": "2024-12-28T14:33:09.477201Z",
    "due_date": "2024-12-28T14:33:06Z",
    "assigned_to": 1,
    "project": 2
  }
  ```

---

### **Partially Update a Task**

  `PATCH` - `http://127.0.0.1:8000/api/tasks/<task_id>/`
  Using this API, only "Admin user" can modify some part of the an individual task info by task_id. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
      "status": "to do"
  }
  ```

---

### **Delete a Task**

  `DELETE` - `http://127.0.0.1:8000/api/tasks/<task_id>/`
  Using this API, you can delete an individual task info from the database by project_id. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

---

## Comment Management

### **Create a Comment**

  `POST` - `http://127.0.0.1:8000/api/comments/`
  you can create a new comment information. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
    "content": "Hey! What about the comments section man!!",
    "user": 2,
    "task": 2
  }
  ```

---

### **Get All Comments**

  `GET` - `http://127.0.0.1:8000/api/comments/`
  This API will retrive all the existing comments data list available in the database. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

---

### **Get a Single Comment**

  `GET` - `http://127.0.0.1:8000/api/comments/<comment_id>/`
  Based on task_id, this API will retrive an individual comment info from the database. This API is accessible to both "Admin" and "member" users.
Note: You need to add "JWT access token" in the bearer token header field.

---

### **Fully Modify a Comment**

  `PUT` - `http://127.0.0.1:8000/api/comments/<comment_id>/`
  Using this API, only "Admin users" can fully modify all the field of the an individual comment info by task_id. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
    "content": "Hi there! What about the comments section man!!",
    "user": 2,
    "task": 2
  }
  ```

---

### **Partially Update a Comment**

  `PATCH` - `http://127.0.0.1:8000/api/comments/<comment_id>/`
  Using this API, only "Admin user" can modify some part of the an individual comment info by task_id. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

  ```json
  {
      "content": "Hi folks! What about the comments section man!!"
  }
  ```

---

### **DELETE**: Delete a Comment

  `DELETE` - `http://127.0.0.1:8000/api/comments/<comment_id>/`
  Using this API, you can delete an individual comment info from the database by project_id. This API is accessible to both "Admin" and "member" users.
  Note: You need to add "JWT access token" in the bearer token header field.

---

## Notes

- Replace `<token>` with your JWT access token in all requests.
- Replace `<project_id>`, `<task_id>`, and `<comment_id>` with the respective resource IDs.

---




