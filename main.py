class Question:

    def __init__(self,prompt,answer):

        self.prompt=prompt

        self.answer=answer
        
        class Quiz:

            def __init__(self):
                self.questions =[]

                self.score = 0
                def add_question(self,question):

                    self.questions.append(question)

                    def take_quiz(self):
                        print("\nPlease answer the following questions:\n" )
                        self.score=0 #Reset score for a new quiz 

                        for question in self.questions:
                            user_answer= input(question.prompt)

                            if user_answer.lower() ==question.answer.lower():
                                self.score+=1

                                print(f"\nYour score:{self.score}/{len(self.questions)}")

                                self.display_results()

                                def display_results(self):
                                    if self.score ==len(self.questions):
                                        print("Perfect score! Great job")

                                    elif self.score >=len(self.questions) / 2:

                                        print("Good job!Keep practicing.")

                                    else:
                                        print("You might want to study more.")
                                        def main():
                                            quiz =Quiz ()
                                            #sample questions

                                            questions =[
                                                Question("what is the capital of france","Paris"),

                                                Question("what is 2+2? ", "4"),

                                                Question("what is the largest planet of our splar sysytem?","Jupiter"),

                                                Question("what programming language is known for its snake logo?","Python"),

                                                Question("Who wrote 'Romeo and Juliet'","Shakesphere"),                                        
                                                  ]
                                            for question in questions:
                                                quiz.add_question(question)

                                                while True:

                                                    print("\n---Exam Preparation App ---")

                                                    print("1.Take the Quiz")

                                                    print("2.Add a New Question")

                                                    print("3.Exit")

                                                    choice=input("Select an option (1-3):")

                                                    if choice =='1':

                                                        quiz.take_quiz()
                                                    elif choice =='2':
                                                        prompt+input("Enter the question: ")

                                                        answer =input("Enter the answer:")

                                                        quiz.add_question(Question(prompt,answer))

                                                        print("Question added succesfully!")

                                                    elif choice=='3':
                                                        print("Exiting the app.Good luck with your studies!")

                                                        break
                                                    else:
                                                        print("Invalid option,please try again.")

                                                        if __name__=="__main__":
                                                            main()

                                                                                                             