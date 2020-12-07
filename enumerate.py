'''
The Python enumerate() function adds a counter to an iterable object. enumerate() function can
accept sequential indexes starting from zero.
'''
subjects = ('Python', 'Interview', 'Questions')
for i, subject in enumerate(subjects):
    print(i, subject)