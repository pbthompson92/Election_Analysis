# Election Analysis

## Overview of Election Audit 
The purpose of this election audit is to quickly analyze the results of a congressional election so that they can be submitted to the election commission for review. This includes taking raw data of individual ballots, in a CSV format, and easily identifying various results, including the winning candidate by vote count and percentage, the turnout by county, and more. 

## Election-Audit Results 
Below is a bulleted list of results from this congressional election. A screen shot from the output of the associated python script is also included to demonstrate the impact this and similar python scripts could have in the future.  

* There was a total of 369,711 votes cast in this congressional election. 
* The breakdown of votes by percentage and count across the various counties can be seen below:
  * Jefferson county had 10.5% of total votes, the equivalent of 38,855 votes. 
  * Denver county had 82.8% of total votes, the equivalent of 306,055 votes. 
  * Arapahoe county had 6.7% of total votes, the equivalent of 24,801 votes. 
* The county with the largest number of votes was Denver.
* The breakdown of votes by percentage and count across the various candidates can be seen below: 
	* Charles Casper Stockham received 23.0% of all votes, the equivalent of 85,213 votes. 
	* Diana DeGette received 73.8% of all votes, the equivalent of 272,892 votes. 
	* Raymon Anthony Doane received 3.1% of all votes, the equivalent of 11,606 votes. 
* The winning candidate was Diana DeGette, with a total of 272,892 votes. This represents 73.8% of all votes cast. 
  
  ![Election Results](https://user-images.githubusercontent.com/91712554/139599051-347a6a37-c2b1-4a01-a012-5aa6d29fe4fc.png)
  
## Election-Audit Summary 
As can been seen in the above screen shot, this script can be incredibly useful for quickly analyzing large amounts of data and creating a clear and concise output of the results of an election. This script could be modified to be used on a larger, national, scale, by changing counties to states. In addition, it could be used to compare Diana to other candidates if she wanted to run for another office in the future. Using this script to run an analysis on a competitor's congressional race would identify counties they are weak in versus counties where they are the favorite. Having an understanding of a competitor's strength and weaknesses would allow for a more targeted campaign to be run.
