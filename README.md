# Top 100 books collector

## How it works?
Script connect to *http://lubimyczytac.pl/ksiazki/popularne/* and grab each data in div *book* next connect to database and send before grabbed data via **PyMySQL**

## Running
To run script you must have installed:
  - Python version >= 3
  - Module BeautifulSoup *(install via pip)*
  - Module PyMySQL *(install via pip)*
  - Have database *(or redo script and save data to file)*

When you download script, you must change database login parameters in *main.py* like:  
```python
db = Database('host','database_user','database_name')
```
## Bugs
404 Not found  ʕ ♥ ‿ ♥ ʔ
