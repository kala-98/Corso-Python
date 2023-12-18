
import json 

with open("bonus/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)
count = 0
while True:
  try:   
    for question in data:
        # mostro le domande
        print(question["question_text"])
        # mostro le possibili risposte
        for index, answer in enumerate(question["alternatives"], 1):
            print(f"{index} - {answer}")
        answer = int(input("Enter your answer: "))
        print("\n" + "=" * 20 + "\n")
        
        if answer == question["correct_answer"]:
            count += 1

    print(f"Your score is {count}/2")
    break

  except ValueError:
    print("You have to insert a number!")
    continue


