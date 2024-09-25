'''
from Student import Student

Student1=Student("Saumya","CSE",7.8,False)
Student2=Student("Jim","IT",8.9,True)
print(Student2.cgpa)
'''

git init

from Question import Question

question_prompts =[
    "what colors are apples?\n(a) Blue\n(b) Red\n(c) Green\n\n",
    "what color are mangoes?\n(a) Red\n(b) Pink\n(c) Yellow\n\n"
]

questions =[
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c")
]


def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)