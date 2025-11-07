'''
You're a hungry rabbit, and you already have eaten a certain number of carrots,
but now you need to eat more carrots to complete the day's meals.
You should return an array of [ total number of eaten carrots after your meals,
                                the number of carrots left after your meals ]
If there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
Example:
* eat(5, 6, 10) -> [11, 4]
* eat(4, 8, 9) -> [12, 1]
* eat(1, 10, 10) -> [11, 0]
* eat(2, 11, 5) -> [7, 0]
Variables:
@number : integer
    the number of carrots that you have eaten.
@need : integer
    the number of carrots that you need to eat.
@remaining : integer
    the number of remaining carrots that exist in stock
Constrain:
* 0 <= number <= 1000
* 0 <= need <= 1000
* 0 <= remaining <= 1000
Have fun :)
'''
def eat(number, need, remaining):
    # Calculate how many carrots can be eaten
    carrots_to_eat = min(need, remaining)
    # Total carrots eaten is the sum of already eaten and newly eaten
    total_eaten = number + carrots_to_eat
    # Remaining carrots after eating
    carrots_left = remaining - carrots_to_eat
    return [total_eaten, carrots_left]