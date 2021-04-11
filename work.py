math_question = [{
    'question': "what is the result of 12*15?",
    'variants': ["240", "180", "210"],
    'correct_answer': "b"},
{
    'question': "What digits represent the following number: sixty-eight million, five hundred two?",
    'variants': ["68,000,502", "68,000,052", "68,005,002"],
    'correct_answer': "a"},
{
    'question': "How many hours are in 1/3 of a day?",
    'variants': ["6", "8", "4"],
    'correct_answer': "b"}]
geography_questions = [{
    'question': "What is the capital of Thailand?",
    'variants': ["Ottawa", "Bangkok", "Madrid"],
    'correct_answer': "b"},
{
    'question': "Madagascar is surrounded by which ocean?",
    'variants': ["Atlantic ocean", "Pacific ocean", "Indian ocean"],
    'correct_answer': "c"},
{
    'question': "Which is the largest country in the world?",
    'variants': ["Russia", "USA", "China"],
    'correct_answer': "a"}]
chemistry_questions = [{
    'question': "What is H20 more commonly known as?",
    'variants': ["water", "hydrogen", "gold"],
    'correct_answer': "a"},
{
    'question': "What is the chemical symbol for gold?",
    'variants': ["Fe", "G", "Au"],
    'correct_answer': "c"},
{
    'question': "K is the chemical symbol for which element?",
    'variants': ["potassium", "hydrogen", "calcium"],
    'correct_answer': "a"}]


def questions(questions):
    correct_answers = 0
    wrong_answers = 0
    answer_variants = ['a', 'b', 'c']
    for index, question in enumerate(questions):
        print(str(index+1) + '. ' + question["question"])
        for variant_index, variant in enumerate(question["variants"]):
            print(answer_variants[variant_index] + ') ' + variant)
        answer = input("Type your answer: ")
        if answer == question["correct_answer"]:
            print("Your answer is correct!!!")
            correct_answers += 1
        else:
            print("Your answer is incorrect!!!")
            wrong_answers += 1
    return correct_answers, wrong_answers


subject = input("Please choose your subject ( M(math), G(geography), CH(chemistry): ")
if subject == 'M':
    correct_answers, wrong_answers = questions(math_question)
    print(f'Your total score is {correct_answers}')
if subject == 'G':
    correct_answers, wrong_answers = questions(geography_questions)
    print(f'Your total score is {correct_answers}')
if subject == 'CH':
    correct_answers, wrong_answers = questions(chemistry_questions)
    print(f'Your total score is {correct_answers}')
