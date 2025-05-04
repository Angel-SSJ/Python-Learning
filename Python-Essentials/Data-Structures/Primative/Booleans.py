

# BOOLEAN #
# zero is false and  any other number is true
# empty strings  are false
done = True
print(type(done) == bool)

print('yes') if done else print('no')

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
# the any function returns true if any of the values in the list is true

ingredient_purchased = True
meal_cooked = False
ready_to_serve = all([ingredient_purchased, meal_cooked])
# the all function returns true if all of the values in the list is true