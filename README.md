# MapReduce using Hadoop

Brief about this project

**MapReduce** is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster. A MapReduce program is composed of a _Map()_ procedure (method) that performs filtering and sorting (such as sorting students by first name into queues, one queue for each name) and a _Reduce()_ method that performs a summary operation (such as counting the number of students in each queue, yielding name frequencies). Following project illustrates discussed concepts using two datasets which are: 
 * _ItemPurchases.csv_
 * _UserDemographicInformation.csv_ (They are both attached in the same repository.)
 
 We will use them to try figuring out how many countries was each product sold in. **Without using any kind of Data Structures**.
 
### System Architecture ( Which this project was developed over)
* Processor type: Intel &reg; Core&trade; i5-2410 CPU @ 2.30Ghz x 4
* Memory: 7.7 GiB

### System Requirements:
* Python 2.7 environment installed
* Hadoop 2.8.1 environment installed

### Design
Entire project is designed using Python 2.7 where I used only some _stdin_ and _stdout_ statements. Major components of this project are:
* mapper-1: maps the mentioned datasets into the following format:
```
U-1019,P-2,-
U-1003,P-2,-
U-1009,P-3,-
U-1004,P-5,-
U-1018,P-1,-
U-1006,P-1,-
U-1011,P-1,-
U-1016,P-5,-
U-1002,P-4,-
U-1005,P-2,-
U-1016,P-3,-
U-1004,P-3,-
U-1015,P-4,-
U-1011,P-4,-
U-1006,P-4,-
U-1014,P-5,-
U-1010,P-2,-
.
.
.
.
U-1008,-,Ecuador
U-1009,-,Albania
U-1010,-,Egypt
U-1011,-,Argentina
U-1012,-,Albania
U-1013,-,Argentina
U-1014,-,Anguilla
U-1015,-,Egypt
U-1016,-,Andorra
U-1017,-,Argentina
U-1018,-,Afghanistan
U-1019,-,Anguilla
U-1020,-,Andorra

```
* reducer-1: reduces _(After applying any sorting algorithm to the mapper output)_ the above format into the following:
```
P-4,Argentina
P-5,Argentina
P-5,Argentina
P-1,Argentina
P-2,Argentina
P-4,Argentina
P-4,Argentina
P-2,Angola
P-2,Angola
P-3,Angola
P-3,Angola
P-4,Angola
P-2,Albania
P-3,Albania
.
.
.

P-4,Argentina
P-5,Argentina
P-5,Argentina
P-1,Argentina
P-2,Argentina
P-4,Argentina
P-4,Argentina
P-2,Angola
P-2,Angola
P-3,Angola
P-3,Angola
P-4,Angola
P-2,Albania
P-3,Albania
```
* mapper-2 _(Important)_: acts as a bridge to the next reducer *(reducer-2)* since hadoop only sorts automatically input of reducers not mappers and we need output of _reducer-1_ to be sorted which we cannot do without using data structures.
So we just print the input of _mapper-2_ and we take advantage that hadoop will sort its output to _reducer-2_. Output of _mapper-2_ is:
```
P-1,Afghanistan
P-1,Albania
P-1,Albania
P-1,Andorra
P-1,Andorra
P-1,Anguilla
P-1,Argentina
P-1,Argentina
P-1,Argentina
P-1,Argentina
P-1,Argentina
P-1,Ecuador
P-1,Ecuador
P-1,Egypt
P-1,Egypt
P-1,Egypt
P-1,Egypt
P-2,Afghanistan
P-2,Albania
P-2,Andorra
P-2,Andorra
P-2,Angola
.
.
.
P-4,Egypt
P-4,Egypt
P-5,Albania
P-5,Albania
P-5,Albania
P-5,Albania
P-5,Albania
P-5,Andorra
P-5,Andorra
P-5,Andorra
P-5,Anguilla
P-5,Anguilla
P-5,Argentina
P-5,Argentina
P-5,Argentina
P-5,Argentina
P-5,Ecuador
P-5,Egypt
P-5,Egypt
```
* reducer-2: sums the distinct countries of each product and output the result as the following:
```
P-1         6
P-2	       8
P-3	       7
P-4	       5
P-5	       6
```
### How-to
We first need to make our mappers and reducers executable.
```
chmod +x /path/to/this_project/mapper-1.py
chmod +x /path/to/this_project/reducer-1.py
chmod +x /path/to/this_project/mapper-2.py
chmod +x /path/to/this_project/reducer-2.py
```
Run hadoop
```
cd $HADOOP_HOME
```
```
sbin/start-all.sh
```
We then need to make directory in hadoop distributed file system _(hdfs)_  of out project and then create an input directory to store our input data in it.
```
hadoop dfs -mkdir -p /project/input
```
Then we move our input into _input_ folder
```
hadoop dfs -put /path/to/this_project/input_data/*.csv /project/input/
```
Now run the first job as the following using _hadoop-streaming-2.8.1.jar_:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar \
-input /project/input/*  \
-output /project/output 
-file /path/to/this_project/mapper-1.py \
-mapper mapper-1.py 
-file /path/to/this_project/reducer-1.py 
-reducer reducer-1.py
```
Please refer to output of _reducer-1_ to visualize it.
We now run the second job and give the output of the previous job as input to the next job in order to obtain the intended result.
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.1.jar \
-input /project/output/  \
-output /project/output2 
-file /path/to/this_project/mapper-2.py \
-mapper mapper-2.py 
-file /path/to/this_project/reducer-2.py 
-reducer reducer-2.py
```
And that's it.
### Issues
Please for any code issues feel free to submit an issue to this repository and I will answer shortly.