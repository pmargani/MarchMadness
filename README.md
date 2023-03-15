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

See results.txt to see the ASCII art bracket

