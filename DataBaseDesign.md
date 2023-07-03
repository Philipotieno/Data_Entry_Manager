## Database Design and Relationships

[![Design Diagram](https://github.com/Philipotieno/Data_Entry_Manager/blob/main/Data%20Entry%20Manager.jpg)]
## Entities:

### User:
- Id (Primary Key)
- Name
- LastName
- Email
- UserName
- Password
- CreatedAt
- UpdatedAt
- Enabled

### Category:
- Id (Primary Key)
- UserId (Foreign Key referencing User.Id)
- Description
- CategoryName
- CreatedAt
- UpdatedAt

### CategoryDetails:
- Id (Primary Key)
- UserId (Foreign Key referencing User.Id)
- CategoryId (Foreign Key referencing Category.Id)
- Name
- Value
- CreatedAt
- UpdatedAt

### Relationships:
- One User can have multiple Categories (One-to-Many relationship)
- One User can have multiple CategoryDetails (One-to-Many relationship)
    - Catagory details should be added to existing categories
- One Category can have multiple CategoryDetails (One-to-Many relationship)




