import sqlite3

db = sqlite3.connect("backend/brandsentinel.db")

tables = db.execute(
    "SELECT name FROM sqlite_master "
    "WHERE type='table' "
    "AND name NOT LIKE 'sqlite_%'"
).fetchall()

print("FOREIGN KEY RELATIONSHIPS")

for (table,) in tables:
    print(f"\nTable: {table}")

    relationships = db.execute(
        f"PRAGMA foreign_key_list({table})"
    ).fetchall()

    if relationships:
        for relationship in relationships:
            print(relationship)
    else:
        print("No foreign keys")

db.close()