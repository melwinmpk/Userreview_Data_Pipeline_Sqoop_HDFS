<h2>Objective</h2>

<b>To solve the some of the use case of the Data PipeLine </b>

<h3><b>Scenario</b></h3>

<p>There is a Famous Restaurant Owner who wants to know how much his overall rating of each item that is sold in his restaurants. <br> He is owning many branches in Kerala, Karnataka, TamilNadu. <br> As the data is not stored in an appropriate format he approaches the Data Engineer to process the Data from him as per his requirement</p>

<h3><b>Input :</b></h3>
<p>given three csv's stored in this format</p>
<p><i><b>"So_no","Customer","ItemId","Rating"</b></i></p>

<h3><b>Output :</b></h3>
<p>The Owner wants to store it in two Data Base Tables </p>
<p><b>Table 1 => Userreview</b> => where all the Users review will be stored irrespective of the region.</p>
<p><b>Table 2 => Item_review_rating</b> => Item wise the Review rating Aggregate will be stored.</p>

<p>The Owner also wants to store this table in HDFS as well.</p>

<h3><b>My Approach :</b></h3>
<ul>
<li>Using python read the CSV file one by one insert the record directly in the Userreview Table and calculate the aggregate of the Rating Item wise update it in the Item_review_rating Table </li>
<li>Using the Sqoop write the command to Insert Entire Data Base into the HDFS </li>
<li>Write a common shell script that executes Python and the Sqoop in one file execution</li>
</ul>

<h3><b>Screenshots</b></h3>
<img src="https://github.com/melwinmpk/Userreview_Data_Pipeline_Sqoop_HDFS/blob/main/img/execution_part1.PNG?raw=true">
<img src="https://github.com/melwinmpk/Userreview_Data_Pipeline_Sqoop_HDFS/blob/main/img/execution_part2.PNG?raw=true">
<img src="https://github.com/melwinmpk/Userreview_Data_Pipeline_Sqoop_HDFS/blob/main/img/SQL_TABLES.PNG?raw=true">
<img src="https://github.com/melwinmpk/Userreview_Data_Pipeline_Sqoop_HDFS/blob/main/img/HDFS_FILES.PNG?raw=true">
