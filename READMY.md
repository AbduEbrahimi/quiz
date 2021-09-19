# quiz

The quiz module runs in the terminal.

It has commands for:
Start the game by asking questions and displaying options.
Show all questions in the database.
Manually change or delete questions and answers with the terminal.
Add manual questions and answers in the terminal.
Add a set of questions and answers with a text file.

There is a text file in the folder where you can put questions, options and answers and enter the database.

Important: Be sure to pay attention to the sample question in the text file.

## Usage

```python
import quiz

# When you enter the module, the game runs and waits for your commands.
>>> import quiz
Welcome to the Quiz Terminal game
call help to see all the commands.
call start to start the game.
؟:

# Enter the start command to start playing the quiz
# Your score will be displayed at the end
؟:start
How many questions do you play?
5
-------------------------Question1-------------------------
Name the Coffee shop in US sitcom Friends? 

option 1: Caffeine Dreams, option 2: Central Perk, option 3: Brewing Beans

The answer is:

# You can use the help command to view all the commands you can enter
؟:help
start : You start the game with no points.
q or quit :  Exits the game without displaying points.
show : You will see all the questions accompanying the question ID.
add : Enters the question into the database sorted by the terminal.
update : You enter the file of questions in the folder into the database.
edit : Receives an ID and you can edit the question.
delete : Receives an ID and deletes the question.

# You need the question ID in the database to delete or edit.
# To get it, write the show in the command to see all the questions with the ID.
؟:show
1  :  What was the Turkish city of Istanbul called before 1930?
2  :  Name the Coffee shop in US sitcom Friends
3  :  How many human players are there on each side in a polo match?
4  :  In what year did Tony Blair become British Prime Minister?
5  :  What is the capital of New Zealand?
6  :  What element is denoted by the chemical symbol Sn in the periodic table?
7  :  What was the most popular girls name in the UK in 2019?
8  :  What is the currency of Denmark?
9  :  How many films have Al Pacino and Robert De Niro appeared in together?
10  :  Who wrote the novels Gone Girl and Sharp Objects?
11  :  How many teeth does the average adult human have?
12  :  How many countries still have the shilling as currency?
13  :  What’s the hardest rock?
```

## Contributing
Pull requests are welcome.

## License
Apache License 2.0
