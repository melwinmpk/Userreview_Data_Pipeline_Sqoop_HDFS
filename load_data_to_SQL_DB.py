import csv
import logging
import random
import mysql.connector as connection
import sys

logging.basicConfig(filename="logdata17thDec.txt")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class regionfood:
    
    def __init__(self,data_path,region,randomseed):
        self.path = data_path
        random.seed(randomseed)
        self.region = region

    def create_data(self):
        # Created the Data in CSV 
        header = ["So_no","Customer","ItemId","Rating"]
        Rating = [1, 2, 3, 4, 5]
        itemid = [1,2,3,4,5]
        customer = [1,2,3,4,5,6,7,8,9,10]
        data = []
        rows = []
        
        for i in range(10):
            rows.append([i+1,"Customer"+str(random.choice(customer)),random.choice(itemid),random.choice(Rating)])
        
        with open(f'{self.path}/region{self.region}.csv',mode='w', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            csvwriter.writerows(rows) 
        
        self.writedata_to_sql()

    def sqlconnect(self):
        self.mydb = connection.connect(host="localhost", database = "Restaurant_db",
                             user="root", passwd = "Welcome@123", use_pure=True)
        self.mydb_cursor = self.mydb.cursor()
        
    def writedata_to_sql(self):
        self.sqlconnect()
        rows = ""
        itemrating = {}
        
        with open(f'{self.path}/region{self.region}.csv',mode='r', newline="") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            
            for row in reader:
                rows += f"('{row[1]}',{row[2]},{row[3]}),"
                if row[2] in itemrating.keys():
                    itemrating[row[2]][int(row[3])] += 1
                else:
                    itemrating[row[2]] = {1:0,2:0,3:0,4:0,5:0}
                    itemrating[row[2]][int(row[3])] += 1
            rows = rows[:-1]
            
        query = f"INSERT INTO Userreview (customer,itemid,rating) VALUES {rows};"
        self.mydb_cursor.execute(query)
        print(f"INSERTED THE RECORD OF THE REGION {self.region}")
        
        for key,item in itemrating.items():
            query =f'''
                       UPDATE Item_review_rating 
                       SET one_star = one_star + {item[1]},
                           two_star = two_star + {item[2]},
                           three_star = three_star + {item[3]},
                           four_star = four_star + {item[4]},
                           five_star = five_star + {item[5]},
                           avg_rating = ((one_star + {item[1]})*1+ (two_star + {item[2]})*2 + (three_star + {item[3]})*3 + (four_star + {item[4]})*4 + 
                                        (five_star + {item[5]})*5)/
                                        (one_star + {item[1]}+two_star + {item[2]}+three_star + {item[3]}+four_star + {item[4]}+five_star + {item[5]})
                        WHERE itemid = {key};
                    '''
            self.mydb_cursor.execute(query)
        print(f"UPDATE THE ITEM REVIEW RATING")
        self.mydb.commit()  
        self.mydb.close()

if __name__ == '__main__':
	try:
	    karnataka_region = regionfood('/home/saif/LFS/cohart-8/17thDecAssignment','Karnataka',50)
	    karnataka_region.writedata_to_sql()
	    Kerala_region = regionfood("/home/saif/LFS/cohart-8/17thDecAssignment","Kerala",0)
	    Kerala_region.writedata_to_sql()
	    TamilNadu_region = regionfood("/home/saif/LFS/cohart-8/17thDecAssignment","TamilNadu",33)
	    TamilNadu_region.writedata_to_sql()
	except Exception as e: 
	    logger.error(f"Oops! {e.__class__} occurred.")
	else:
	    logger.info("Writing Data to sql Executed Successfully") 
