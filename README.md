# LotterySpider Project

This is a spider project for getting data automatically from lottery website and sending it to database.

## Spdier Part

Using selenium as spider


## Database Part

this branch we use object-oriented way to implement two part , thus we can add another table just **inherit the abstract Table class**

### For example

#### 1.first add Mytable class inherited from Table
```python3
class MyTable(Table):
	@property
	def filename(self):
		return 'mytablename.csv'

	@property
	def insert_sql(self):
		return "INSERT INTO MY_TABLE (ID,...) VALUES "

	# get title column and data from mytablename.csv
	def get_data(self):
		with open(wd+'\\'+self.filename) as f:
			reader = csv.reader(f)
			contents = [i for i in reader]
		#get date from csv
		date = contents[2][1][:10]
		# get data from csv
		data = contents[5:20]
		#join data with date
		data_and_date = [i+[date] for i in data]
		return data_and_date

```

#### 2. add new object in main.py

```python3 
from table.py import MyTable

\#mt means mytable and ld means lottery_database

mt = MyTable()
ld.addTable(mt)

```
and you just call ld.insert_date and everything is ok


### lottery_util Part

deal with the csv file 

### operate_oracle Part

deal with the oracle database
