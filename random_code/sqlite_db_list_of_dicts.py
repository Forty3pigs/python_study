import sqlite3

SAMPLE_DB = "sample_db.db" # path to our example database


# Schema defining the table holding our data
SCHEMA = """CREATE TABLE data (fpath TEXT, n_measure INTEGER, treatment TEXT,
                             amplitude REAL)"""

# make the database by connecting
temp_db = sqlite3.connect(SAMPLE_DB)

# Create the table, commit it, and close the connection
temp_db.execute(SCHEMA)
temp_db.commit()
temp_db.close()

test_data = [
      {
          "fpath": "path/to/file/one.dat",
          "n_measure": 1,
          "treatment": "Control",
          "amplitude": 50.5,
      },
      {
          "fpath": "path/to/file/two.dat",
          "n_measure": 2,
          "treatment": "Control",
          "amplitude": 76.5,
      },
      {
          "fpath": "path/to/file/three.dat",
          "n_measure": 1,
          "treatment": "Experimental",
          "amplitude": 5.5,
      },
  ]

temp_db = sqlite3.connect(SAMPLE_DB)  # re-connect to the sample database we just made

for item in test_data:
    temp_db.execute(
        "INSERT INTO data (fpath, n_measure, treatment, amplitude) "
        "VALUES(:fpath, :n_measure, :treatment, :amplitude)",
        item,
    )
    temp_db.commit()  # commit after each addition
    print(f"Added data {item['fpath']}")  # print a helpful message once added

temp_db.close()
# Added data path/to/file/one.dat
# Added data path/to/file/two.dat
# Added data path/to/file/three.dat


temp_db = sqlite3.connect(SAMPLE_DB)
temp_db.row_factory = sqlite3.Row
values = temp_db.execute("SELECT * FROM data").fetchall()

list_accumulator = []
for item in values:
    list_accumulator.append({k: item[k] for k in item.keys()})
print(list_accumulator)

# [{'fpath': 'path/to/file/one.dat',
#   'n_measure': 1,
#   'treatment': 'Control',
#   'amplitude': 50.5},
#  {'fpath': 'path/to/file/two.dat',
#   'n_measure': 2,
#   'treatment': 'Control',
#   'amplitude': 76.5},
#  {'fpath': 'path/to/file/three.dat',
#   'n_measure': 1,
#   'treatment': 'Experimental',
#   'amplitude': 5.5}]
temp_db.close()