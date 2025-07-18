# SQL Introduction

This repository contains SQL scripts demonstrating basic database operations in MySQL.

## Scripts

- **0-list_databases.sql** - Lists all databases
- **1-create_database_if_missing.sql** - Creates database `hbtn_0c_0`
- **2-remove_database.sql** - Deletes database `hbtn_0c_0`
- **3-list_tables.sql** - Lists all tables in a database
- **4-first_table.sql** - Creates table `first_table`
- **5-full_table.sql** - Shows full table description
- **6-list_values.sql** - Lists all rows in table
- **7-insert_value.sql** - Inserts new row
- **8-count_89.sql** - Counts records with specific ID
- **9-full_creation.sql** - Creates `second_table` with sample data
- **10-top_score.sql** - Lists records ordered by score
- **11-best_score.sql** - Lists records with score >= 10
- **12-no_cheating.sql** - Updates specific record
- **13-change_class.sql** - Deletes records with low scores
- **14-average.sql** - Calculates average score
- **15-groups.sql** - Groups records by score
- **16-no_link.sql** - Lists records excluding NULL names

## Usage

```bash
cat script.sql | mysql -hlocalhost -uroot -p [database_name]
```