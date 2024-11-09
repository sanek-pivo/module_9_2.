first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable'] # по условию
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler'] # по условию

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result) # список из длин строк не менее 5 символов

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result) # список сборки кортежей, слово из одного списка сравнивается со вторым

third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print(third_result) # созданный словарь, где значения строк будут перебираться из объединённых вместе