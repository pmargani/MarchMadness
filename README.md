# MarchMadness
A simple script for determing March Madness results from coaches' salaries


## Intro

Predicting the first round of results for the 2022 World Cup using each countries GDP was a lot of fun (though finding the GDP of Wales separate from the UK was a pain).  So I thought I'd take a try at the same approach for March Madness.

The amount of APIs and web sites that provide this kind of information was kind of overwhelming, so I took a simpler approach, hard coding the teams for this year (2023), and using a tab-deliminated file for the coachs' salaries (seeded by a particular web-site).

I couldn't fill in all the gaps: where there is no salary associated with a team, I used the average from the provided data.

## Installation

No special packages are needed.  Simply:

python marchMadness2023.py NCAACoachSalaries.txt

## Results

For 2023, Duke wins!

num teams in bracket:  64
num teams with salaries:  93
num teams in bracket with no salary:  14
Number of games decided by salaries:  45
Number of games decided lacking salary info:  18
Average Salary: $2.219M

West Bracket
Kansas ($4.780M)
               Kansas ($4.780M)
Howard ($3.400M)
                              Kansas ($4.780M)
Arkansas ($2.550M)
               Illinois ($2.755M)
Illinois ($2.755M)
                                             Kansas ($4.780M)
Saint Mary's (avg)
               Saint Mary's (avg)
VCU ($1.700M)
                              UConn ($2.750M)
UConn ($2.750M)
               UConn ($2.750M)
Iona ($0.511M)
                                                            Kansas ($4.780M)
TCU ($4.300M)
               TCU ($4.300M)
Arizona State ($2.100M)
                              TCU ($4.300M)
Gonzaga ($1.934M)
               Grand Canyon (avg)
Grand Canyon (avg)
                                             TCU ($4.300M)
Northwestern ($1.435M)
               Northwestern ($1.435M)
Boise State ($0.900M)
                              UCLA ($2.600M)
UCLA ($2.600M)
               UCLA ($2.600M)
UNC Asheville (avg)


South Bracket
Alabama ($2.899M)
               Alabama ($2.899M)
Texas A&M ($2.350M)
                              West Virginia ($3.750M)
Maryland ($2.701M)
               West Virginia ($3.750M)
West Virginia ($3.750M)
                                             West Virginia ($3.750M)
San Diego State ($0.755M)
               San Diego State ($0.755M)
Charleston ($0.600M)
                              Virginia ($3.000M)
Virginia ($3.000M)
               Virginia ($3.000M)
Furman (avg)
                                                            West Virginia ($3.750M)
Creighton ($1.327M)
               NC State ($3.340M)
NC State ($3.340M)
                              NC State ($3.340M)
Baylor ($2.866M)
               Baylor ($2.866M)
UC Santa Barbara (avg)
                                             Arizona ($3.655M)
Missouri ($2.700M)
               Missouri ($2.700M)
Utah State (avg)
                              Arizona ($3.655M)
Arizona ($3.655M)
               Arizona ($3.655M)
Princeton (avg)


East Bracket
Purdue ($2.479M)
               Purdue ($2.479M)
TX Southern (avg)
                              Memphis ($2.750M)
Memphis ($2.750M)
               Memphis ($2.750M)
Florida Atlantic (avg)
                                             Duke ($8.982M)
Duke ($8.982M)
               Duke ($8.982M)
Oral Roberts (avg)
                              Duke ($8.982M)
Tennessee ($2.250M)
               Louisiana ($3.000M)
Louisiana ($3.000M)
                                                            Duke ($8.982M)
Kentucky ($7.450M)
               Kentucky ($7.450M)
Providence ($2.204M)
                              Kentucky ($7.450M)
Kansas State ($2.250M)
               Kansas State ($2.250M)
Montana State ($0.547M)
                                             Kentucky ($7.450M)
Michigan State ($3.653M)
               Michigan State ($3.653M)
USC ($2.200M)
                              Michigan State ($3.653M)
Marquette ($1.200M)
               Marquette ($1.200M)
Vermont ($0.365M)


Midwest Bracket
Houston ($3.000M)
               Houston ($3.000M)
Northern Kentucky (avg)
                              Houston ($3.000M)
Iowa ($2.225M)
               Auburn ($2.500M)
Auburn ($2.500M)
                                             Indiana ($3.200M)
Miami ($1.500M)
               Miami ($1.500M)
Drake ($0.334M)
                              Indiana ($3.200M)
Indiana ($3.200M)
               Indiana ($3.200M)
Kent State ($0.285M)
                                                            Indiana ($3.200M)
Iowa State ($2.000M)
               Mississippi State ($2.100M)
Mississippi State ($2.100M)
                              Kennesaw State (avg)
Xavier ($1.669M)
               Kennesaw State (avg)
Kennesaw State (avg)
                                             Texas ($3.100M)
Texas A&M ($2.350M)
               Texas A&M ($2.350M)
Penn State (avg)
                              Texas ($3.100M)
Texas ($3.100M)
               Texas ($3.100M)
Colgate (avg)


Final Four Bracket
West Virginia ($3.750M)
               Duke ($8.982M)
Duke ($8.982M)
                              Duke ($8.982M)
Indiana ($3.200M)
               Kansas ($4.780M)
Kansas ($4.780M)

