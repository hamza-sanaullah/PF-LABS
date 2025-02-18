#defining color codes to be use in code
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'
#wrting questionsd
Ecat_Questions = [("1. What's the second name of Quadratic Equation?",GREEN+"a) Second Degree Equation" ,"b) First Degree ""Equation","c) Third degree equation","d) fourth Degree Equation","e) skip"),
("2.What's the meaning of ""chubby?","a)lazy","b)healthy","c)Noisy","d)unhealthy","e)skip",CYAN+"F)Submit"),
("3. Who is the prime minister of canada?","a) Justin Tudo","b)Jobaiden","c)Narendra Modi","d)Imran khan","e)skip",CYAN+"F)Submit"),
("4. How many people are here on earth?","a)2000","b)1arab","c)8 ara","d)5 arab","e)skip","F)Submit"),
("5. what is the derivative of sin",BLUE,"a)tan","b)cos","c)sec","d)cot","e)skip","F)submit"),
("6. Who is the father of mathematics",RED,"a)Archimedes","b)Euler","c)Newton","d)Leibniz","e)skip","F)Submit"),
("7. Who is the father of chemistry",MAGENTA,"a)Antoinie Lavoisier","b)Rutherford","c)Dawton","d)Marie Curie","e)Skip","F)Submit"),
("8. What is the capital of FINLAND?","a)Helsinki","b)Cnberra","Islamabad","Delhi","e)Skip","F)submit"),
("9. what stands for IMF?","a)International Monetary Fund","b)Inter services and Public relations","c)Compressed Natural Gas","d)nothing","e)Skip","F)Submit"),
("10. what is the purpose of ciloxan?","a)eye infection","b)ear protection","c)Stomach pain","d)nothing","e)Skip","F)Submit"),]
correct_answers = ["a", "b", "a", "c", "b", "a", "a", "a", "a", "a"]
correct_ans = 0
skipped_questions = 0
incorrect_answers = 0
score = 0
questions_attempted = 0
unattempted_questions = 0
skipped_list = []
skipped_index = []
#enumerate function loops over both index and question
for index, question in enumerate(Ecat_Questions):
    for option in question:
        print(option)

    user_answer = input("Enter your answer: ").lower().strip()
    if user_answer == "f":
        break
        #checking user answer by comparing correct answers list
    if user_answer ==  correct_answers[index] :
        correct_ans+=1
        score+=4

        ANSWER = "CORRECT"
    else:
        if user_answer!="e":
            incorrect_answers+=1
            score-=1
        ANSWER = "Incorrect"
    if user_answer == "e":
        #appending skip questions and index in a sepoarere list
        skipped_questions+=1
        skipped_list.append(question)
        skipped_index.append(index)


    elif user_answer in correct_answers:
        questions_attempted+=1
    elif user_answer !="e":

        unattempted_questions+=1
#printing skipo questions again by choice of user
if skipped_questions>0:
    skip_attempt = input("Do you want to attempt the skipped questions")
    if skip_attempt.lower() == "yes":
        for index, question in enumerate(skipped_list):
            for option in question:
                print(option)
            user_answer = input("Enter your answer: ").lower().strip()
            if user_answer == correct_answers[skipped_index[index]]:
                correct_ans+= 1
                score += 4
            else:
                    incorrect_answers += 1
                    score -= 1

            if user_answer in correct_answers:
                questions_attempted+=1


            elif user_answer == "f":
                break
            elif user_answer =="e":
                continue


            skipped_questions-=1
    else:
        unattempted_questions+=skipped_questions
else:
    pass



print(f"The amount of correct answers is {BLUE}{correct_ans}")
print(f"The amount of skipped questions is {skipped_questions}")

print(f"The amount of incorrect answers is {RED} {incorrect_answers}")
print(f"your score is {score}")
print(f"THe attempted questions are {MAGENTA}{questions_attempted}")
print(f"THe unattempted questions are {YELLOW}{unattempted_questions}")

if score<12:
    print("you are not eligible for admission in UET")
else:
    print("Congratulations you are selected!")
