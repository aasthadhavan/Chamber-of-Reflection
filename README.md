The Art Gallery Management System is a complete Database Management System (DBMS) mini-project.
It is designed to help an art gallery store and manage details about artists, artworks, galleries, exhibitions, and customers through a user-friendly web interface.
The project demonstrates the integration of a Flask-based backend with a MySQL database, and it is ideal for academic submissions or learning database connectivity.

-TECHNOLOGY STACK

Frontend: HTML, CSS (Jinja2 Templates)

Backend: Python (Flask Framework)

Database: MySQL

Libraries Used: flask, flask-mysqldb

Tools Used: MySQL CMD / Workbench, VS Code / PyCharm

- KEY FEATURES

Add, view, and manage data for Artists, Artworks, Galleries, Exhibitions, Customers, and Contacts

Relational database structure with foreign key relationships

Demonstrates CRUD operations (Create, Read, Update, Delete)

Properly normalized database schema (up to 3NF)

Simple, clean web interface for practical use

Works on localhost and connects to MySQL seamlessly


- DATABASE DESIGN SUMMARY

The database consists of six tables:

Artist – Contains details about artists (name, birthplace, art style)

Artwork – Stores artworks with title, type, price, and linked artist

Gallery – Maintains gallery information such as name and location

Exhibition – Represents exhibitions organized by galleries

Customer – Stores details of art buyers and visitors

Contacts – Contains additional contact info for each customer

Relationships:

One Artist → Many Artworks

One Gallery → Many Exhibitions

One Customer → Many Contacts

Foreign keys ensure referential integrity across tables
