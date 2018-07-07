# Top 100 books collector

## How it works?
Script connect to *https://lubimyczyta.pl/ksiazki/pupularne/* and grab each data in div *book* next connect to database and send before grabbed data via **PyMySQL**

## Running
* To run script you must have installed:
  - Python version >= 3
  - Module BeautifulSoup *(install via pip)*
  - Module PyMySQL *(install via pip)*
  - Have database *(or redo script and save data to file)*

When you download script, you must change database login parameters in *main.py*

## Problems
* **Warning:** *Data truncated for column*
**Solution:** Uncomment line 26 *db.query("ALTER TABLE `top100LC` CHANGE addDate addDate CHAR(34);")* 