user_age = int(input())

webpage = 'about_whiskey.html' if user_age >= 21 else 'sorry.html'

if user_age >= 21:
    webpage = 'about_whiskey.html'
else:
    webpage = 'sorry.html'




