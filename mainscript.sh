#!/bin/sh

. ${1}

echo "RUNNING THE PYTHON CODE TO INSERT THE DATA FROM CSV TO SQL DATA BASE"

python3 load_data_to_SQL_DB.py

if [ $? -eq 0 ]

	then

		echo "INSERT THE DATA FROM CSV TO SQL DATA BASE SUCCESSFULL"
		echo "RUNNING INSERT SQOOP COMMAND TO IMPORT THE DATABASE TO HDFS"

		 sqoop import-all-tables \
		 --connect jdbc:mysql://localhost:${PORT_NO}/${DB_NAME}?useSSL=False \
		 --username root --password-file file:///home/saif/LFS/datasets/sqoop.pwd \
		 --warehouse-dir ${OP_DIR}${DB_NAME} \
		 --autoreset-to-one-mapper

		if [ $? -eq 0 ]

			then
			
				echo "INSERT SQOOP COMMAND TO IMPORT THE DATABASE TO HDFS SUCCESSFULL"
		fi
fi



