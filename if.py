rain = input ('請問今天有沒有下雨? A: ')
if rain == '有':
    print ('撐傘出門')
    print ('買一包洋芋片')
    print ('在家看電影')
if rain != '有':
    print ('Go out and have fun!')

age = input ('please enter your age ==> ')
age = int (age)
if age >= 20:
    print ('you can vote')
else:
    print ('you are not old enough to vote')