import random
import sqlite3 
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'quiz.db')
text_path = os.path.join(BASE_DIR, 'load_file.txt')

""" Play quiz in the terminal environment for fun.
For a quick start, you can enter the "start" command.
You can see all the questions with the "show" command.
To view a guide to all commands, use the "help" command."""

print("Welcome to the Quiz Terminal game")
print("call help to see all the commands.")
print("call start to start the game.")

def help():
    """See all commands that can be used in the game."""
    help = """start: You start the game with no points.
q or quit: Exits the game without displaying points.
show: You will see all the questions accompanying the question ID.
add: Enters the question into the database sorted by the terminal.
update: You enter the file of questions in the folder into the database.
edit: Receives an ID and you can edit the question.
delete: Receives an ID and deletes the question."""
    print(help)


def add():
    """Receives input data from the user
    in the form of Tupel and places them in the database.
    Information can be retrieved with the "add_data" function
    as an argument. If stored in the database, the message that the
    operation was successful will be printed in the terminal. """
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    data = new_data()
    cur.execute("""INSERT INTO per_quiz
        (soual, javab_aval,
        javab_dovom, javab_sevom,
        pasokh) VALUES(?,?,?,?,?)""",
        data)
    print('operation was successful')
    print('---------------------------\n')            
    con.commit()
    con.close()

def new_data():
    """This function returns the questions and answers that
    we want to manually store in the database based on Tupel.
    Information includes:
    1. Question
    2. Option one
    3. Option two
    4. Option three
    5. Answer
    This function cannot put information in the database.
    We must send it as an argument in the "insert_data" function."""
    print('---------------------------')
    soal = input('Question ? \n:')
    print('Enter options :')
    javab_1 = input('1: ')
    javab_2 = input('2: ')
    javab_3 = input('3: ')
    pasokh = input('Answer: ')
    print("enter : save , q : quit")
    save = input(': ')
    if save == "":
        data_to_execute = (soal,javab_1,javab_2,javab_3,pasokh)
        return data_to_execute
    else:
        print("There was a problem receiving information")
        app_run()


def edit_data():
    """Changes the information in the database.
    First, the ID receives the question. It then asks questions and options,
    and finally gets the correct answer and returns a list.
    Is called as a variable in the "edit_quiz" function."""
    print('Please enter the ID')
    id_adad = input(': ')
    found = False
    try:
        id_add = int(id_adad)
    except ValueError:
        print("There was a problem retrieving information from the terminal. Try again")    
        app_run()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    search = cur.execute(""" SELECT id FROM per_quiz """)
    for x in search:
        if id_add in x:
            found = True
    if found:  
        soal_e = input('Question ?\n: ')
        pasoch1 = input('options 1  \n: ')
        pasoch2 = input('options 2  \n: ')
        pasoch3 = input('options 3  \n: ')
        javab = input('Answer  \n: ')
        all_edit = [soal_e,pasoch1,pasoch2,pasoch3,javab,id_adad]
        return all_edit 
    else:
        print("id not found in database")
        app_run()

def edit():
    """Change information with this function.
    It first calls the "edit_data" function as a variable.
    It then changes the information in the
    database according to the variable."""
    data_update = edit_data()
    if data_update == None:
        app_run()
    else:    
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        print("enter : save , q : quit")
        save = input(': ')
        if save == "":
            cur.execute("""
                UPDATE per_quiz SET soual = ?,
                javab_aval = ?, javab_dovom = ?,
                javab_sevom = ?, pasokh = ?
                WHERE id = ? """, (data_update[0],
                data_update[1], data_update[2],
                data_update[3], data_update[4],
                data_update[5]))
            print("Information updated")            
            con.commit()
            con.close()
        else:
            print("! Information not saved !")
            app_run()

def delete():
    """Removes the question from the database.
    Requires a question ID. After deleting from the database,
    the message of this action is displayed."""
    print("Please enter the ID you want to delete")
    delete_id = input(": ")
    try:
        delete_id = int(delete_id)
    except ValueError:
        print("Please use only numbers")
        app_run()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    search = cur.execute(""" SELECT id FROM per_quiz """)
    if delete_id not in search:
        print("id not found in database")
        app_run()
    else:
        cur.execute("""DELETE FROM per_quiz WHERE id = ? """,(delete_id,))
        print("Data successfully deleted")
        con.commit()
        con.close()

def update():
    """Searches within the current directory for a group file of questions.
    This is a simple text file in which the answer questions must be placed
    in a horizontal column and separated by commas.Automatically enters the
    questions in the questions section and the options in the options section
    into the database.After the operation, the message of its success will be
    displayed in the terminal.For newer questions, the previous ones should be
    deleted so that they do not re-enter the database.
    Sample writing in file:
            Question, first option, second option, third option, answer,
    !! Do not forget the comma at the end !! """
    file = open(text_path,'r')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    list_line = file.readlines() 
    all_quiz = []
    for x in range(0,len(list_line)):
        all_quiz.append(list_line[x].split(','))
    for y in range(0,len(all_quiz)-1):    
        cur.execute("""INSERT INTO per_quiz(soual,
        javab_aval,javab_dovom,javab_sevom,
        pasokh) VALUES(?,?,?,?,?)""",(all_quiz[y][0],all_quiz[y][1],
        all_quiz[y][2],all_quiz[y][3],all_quiz[y][4]))            
        con.commit()        
    print(f'all {len(all_quiz)} data saved')
    con.close() 

def show():
    """Browses the database and returns all questions with the ID number.
    If you want to change or update or delete the question,
    you can use the return ID and other functions that the ID needs to do."""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    all = cur.execute(""" SELECT id,soual FROM per_quiz """)
    for a in all:
        print(a[0]," : ",a[1])
    con.close()

def rand_cois(count):
    """Selects questions randomly.
    If the number of requests for your queries exceeds the database inventory,
    the error message will display a large number of queries.
    At the end of the operation returns a list of random numbers
    that are used to select questions."""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    all_db = cur.execute(""" SELECT COUNT() FROM per_quiz """)
    numberOfRows = all_db.fetchone()[0]
    if count >= numberOfRows:
        print("requested questions is more than the database inventory.")
        print('Choose fewer questions.')
        app_run()
    rand_q = random.sample(range(0,numberOfRows),count)
    con.close()
    return rand_q

def start():
    """Randomly displays questions from the database.
    Before we begin, it asks us how many questions we want to answer.
    After entering the answer, he checks it with the correct answer.
    If it is equal, points will be added. If the answer is wrong,
    no points will be awarded and he will go to the next question.
    At the end, points will be seen."""
    global score
    print("How many questions do you play?")
    count_round = input('')
    try:
        count_round = int(count_round)
        if count_round == 0:
            print("You can not enter the number '0'")
            app_run()
    except ValueError:
        print("Just enter a number")     
        app_run()
    rand = rand_cois(count_round+1)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    all_db = cur.execute(""" SELECT id,soual,
                        javab_aval,javab_dovom,
                        javab_sevom,pasokh FROM per_quiz """)
    all_data = all_db.fetchall()
    for d in range(1,count_round+1):
        question = all_data[rand[d]]
        print(f"""
-------------------------Question{d}-------------------------
{question[1]} \n                

option 1: {question[2]}, option 2: {question[3]}, option 3: {question[4]}

""")
        answer = input("The answer is:")
        if answer == question[5]:
            score += 10
            print("Your answer was correct")
        else:
            print("Your answer was a mistake")
        print('-------------------------------------------------------------')
    con.close()
    print("#"*20,f"\nThe questions are over Your score: {score}\n","#"*20)
    score = 0

def app_run():
    print()
    run = input("؟:")
    if run == "help":
        help()
    elif run == "show":
        show()    
    elif run == "start":
        start()
    elif run == "add":
        add()    
    elif run == "q" or run == "quit":
        quit()
    elif run == "edit":
        edit()
    elif run == "delete":
        delete()
    if run == "update":
        update()
    elif run not in list_comm:
        print("commend not found you can use the help commend to see more information")
    
score = 0
list_comm = ("help","add","q","quit","show","delete","edit","update","start")

while True:  
    app_run()
