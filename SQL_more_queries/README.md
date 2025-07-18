# SQL - More Queries

This repository contains advanced SQL scripts demonstrating complex queries, user management, and database relationships in MySQL.

## Scripts

### User Management & Privileges
- **0-privileges.sql** - Lists privileges for specific users
- **1-create_user.sql** - Creates user with all privileges
- **2-create_read_user.sql** - Creates database and read-only user

### Table Creation & Constraints
- **3-force_name.sql** - Creates table with NOT NULL constraint
- **4-never_empty.sql** - Creates table with DEFAULT value
- **5-unique_id.sql** - Creates table with UNIQUE constraint
- **6-states.sql** - Creates states table with PRIMARY KEY and AUTO_INCREMENT
- **7-cities.sql** - Creates cities table with FOREIGN KEY constraint

### Basic Queries
- **8-cities_of_california_subquery.sql** - Lists cities using subquery
- **9-cities_by_state_join.sql** - Lists cities with states using JOIN

### TV Shows Database Queries
- **10-genre_id_by_show.sql** - Shows with at least one genre (INNER JOIN)
- **11-genre_id_all_shows.sql** - All shows including those without genres (LEFT JOIN)
- **12-no_genre.sql** - Shows without any genres
- **13-count_shows_by_genre.sql** - Count shows per genre (GROUP BY, COUNT)
- **14-my_genres.sql** - Genres for specific show
- **15-comedy_only.sql** - Shows in Comedy genre
- **16-shows_by_genre.sql** - All shows with their genres

## Key Concepts Covered

- **User Management**: CREATE USER, GRANT, SHOW GRANTS
- **Table Constraints**: NOT NULL, DEFAULT, UNIQUE, PRIMARY KEY, FOREIGN KEY
- **JOIN Types**: INNER JOIN, LEFT JOIN
- **Advanced Queries**: Subqueries, GROUP BY, COUNT, ORDER BY
- **Database Relationships**: One-to-many, many-to-many

## Usage

```bash
cat script.sql | mysql -hlocalhost -uroot -p [database_name]
```