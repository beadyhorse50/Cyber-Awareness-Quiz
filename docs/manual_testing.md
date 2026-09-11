# Manual Testing REults

Testing was completed on a wWindows 11 device and I used Python 3.14.4, and deployed on Stramlit Cloud version.

 Valid name accepted | I entered a normal name, clicked start quiz| Quiz starts at question 1 |Pass |
Not entering any values for the name | Left the box blank press click Start Quiz | Error shows and quiz does not start |Pass|
A name that has digits does not work | Enter "Todi2" and click Start Quiz | Error about numbers in name |Pass |
You have to pick an answer before continuing | Clicked next without selecting an option | Error shows and stays on same question |Pass |
True or false questions| You have to get to Q6 for these to come up| Two options shown and you pick either True and False |Pass |
Ensure the score is calculated correctly | Answer all 10 counting how many were right | Score matches the number answered correctly |Pass |
 Wrong answers are shown at the end |Answered questions wrong on purpose | Those incorrect answers were listed at the end of the quiz |Pass|
Results are saved to CSV | Complete the quiz then open data/results.csv | New row with name, score, total and date |Pass|
Wrong admin credentials are rejected | Entered the wrong admin password on purpose | "Incorrect password" error and left with no access to results |Pass|