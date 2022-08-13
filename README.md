# PESEL number decoding #
Reading the information contained in the PESEL number.

## Table of Contents: ##
1. General information about the project
2. How the program works?
3. More information

### 1. General information about the project ###

The state system in Poland assigns each citizen a unique PESEL number at the time of birth. PESEL contains basic information such as: gender, day, month and year of birth. The code consists of 11 digits.

### 2. How the program works? ###

- The programmed code first checks if the provided *PESEL number is correct* - it contains only digits and consists of exactly 11 digits. Otherwise, it informs the user that the given number is incorrect.
- Then the code reads the gender, day, month and year of birth from the provided PESEL number.

**Note:** people born after 1999 in the PESEL number have the number 20 added to the month number, hence, for example, a person born in May 2000 in the PESEL number has the month coded as 25, not 5.

### 3. More information ###

More information on how the data in the PESEL number is encoded at the link: [More information](https://pl.wikipedia.org/wiki/PESEL?msclkid=c280547ab59311ecbdceca5de2e00528)

*Author:* Marta Solarz
