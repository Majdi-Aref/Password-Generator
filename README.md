# "create-your-password"
+ "create-your-password" is an implementation is a programme that arbitrarily generates passwords. People who need numerous passwords for their numerous subscriptions would make use of this programme.
+ I developed "create-your-password" as my Portfolio Project 3 for my full stack software development diploma with the Code Institute in Dublin, Ireland.
+ "create-your-password" is the name of the programme on Heroku; however, its name on Github is "Password-Generator". Through this readme.md file, I will apply its name on Heroku, which is "create-your-password"; please take this into your consideration.

# 1. User Stories
+ As a visiting user, I would like to use this program to generate passwords that I can utilize while I will be subscribing online.
+ While creating a password, I, as a visting user, would like to be able to decide whether to include numbers and/or special characters in a password provided that letters comprise the main part of it.

# 2. Existing Features
## 2. 1. First Input Statement
+ As Heroku runs "create-your-password", the first, cyan input statement will be displayed to a user.
+ This first input statment is: "Enter a number that represents the minimum length of the password that you want; the number must be greater than 5."
+ It will encourage a user to type in their preferred number of characters that will comprise the minimum length of their password.
+ It is well worth mentioning that Heroku automatically displays what a user types in as their answer to each input statement.
+ If a user entered a string instead of a number, an error, red message will appear informing a user that they typed in letters and/or special characters; immediately afterwards, the first input statement will once more be displayed prompting a user to enter a number that is greater than 5.
+ If a user entered a number that is not greater than 5 (0 for example), an error, red message will appear informing a user that they typed in a number that is not greater than 5; immediately afterwards, the first input statement will again be displayed prompting a user to enter a number that is greater than 5.
+ As soon as a user enters a number that is greater than 5, the second input statement will be displayed.
+ Please have a look at the relevant images below.

![First input statement 1](readme-images/first-input-statement-1.png)

![First input statement 2](readme-images/first-input-statement-2.png)

![First input statement 3](readme-images/first-input-statement-3.png)

![First input statement 4](readme-images/first-input-statement-4.png)

## 2. 2. Second Input Statement
+ As soons as a user has entered a number that is greater than 5, the second, cyan input statement will be displayed, which asks them to specify if they want to have numbers in their password; if they want to, they must enter a 'y' and if they do not, they must enter an 'n'.
+ If a user entered neither 'y' nor 'n', an error, red message will appear and inform them that they entered neither 'y' nor 'n'; immediately afterwards, the second input statement will be one more time demonstrated reminding a user that they must enter either 'y' or 'n'.
+ As soon as a user has entered a 'y' or 'n', the third input statement will come into view.
+ Please consider the image below, which illutstrates all the scenarios above.

![Second input statement](readme-images/second-input-statement.png)

## 2. 3. Third Input Statement & Password Generation
+ Once a user has entered a 'y' or an 'n' as their answer to the second input statement, the third input statement will emerge requesting an explanation as to whether they want to have special characters in their password; if they want to, they must enter a 'y' and if they do not, they must enter an 'n'.
+ If a user entered neither 'y' nor 'n', an error, red message will appear and inform them that they entered neither 'y' nor 'n'; immediately afterwards, the second input statement will be one more time demonstrated reminding a user that they must enter either a 'y' or an 'n'.
+ When a user has entered a 'y' or an 'n', a green message will arise, which is: "Your requested password is:" and the requested password will be revealed in a new line in yellow.
+ Beneath is a relevant image.

![Third input statement & password generation](readme-images/third-input-statement.png)

# 3. Future Features
+ I would develop an option in which a user could single out how difficult a password should be.
+ If I could, I would incorporate the letters, numbers, and special characters of many languages in addition to English.
+ Ordering several passwords simultaneously from the very start of the programme.

# 4. Typography & Color Scheme
+ I utilized the typography that is incorporated in Heroku.
+ As for the color scheme of the programme, I imported "colorama", installed it into my Codeanywhere's workspace, and added it into the requirements.txt file so that Heroku can execute the color settings of "colorama" on the "create-your-password" programme.
+ The input statements questions and a user's answers are in cyan.
+ The error messages are in red.
+ The "Your requested password is:" message is in green.
+ The message that reveals the requested password is in yellow.
+ Kindly check the image down below that shows the color scheme of the programme.

![Color scheme](readme-images/color-scheme.png)

# 5. Flowcharts
+ Underneath is the flowchart of "create-your-password" programme.

![Flowchart](readme-images/flowchart.png)




