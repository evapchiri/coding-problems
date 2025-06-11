# # You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

# Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

# For example, given the following map, where you are x, coins are o, and empty spaces are . (top left is 0, 0):
# return (0, 4), since that coin is closest. This map would be represented in our question as:

# ---------------------
# | . | . | x | . | o |
# ---------------------
# | o | . | . | . | . |
# ---------------------
# | o | . | . | . | o |
# ---------------------
# | . | . | o | . | . |
# ---------------------

# Our position: (0, 2)
# Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]


# ---------------------
# | . | . | . | . | . |
# ---------------------
# | o | . | . | x | . |
# ---------------------
# | o | . | o | . | o |
# ---------------------
# | 0 | . | o | . | . |
# ---------------------


## O(n log n) time complexity bc of sort()

# def closest_coin(coins: list, position: tuple):

#     movements_to_coins = {}

#     for coin_position in coins:

#         x_axis = abs(coin_position[0] - position[0])
#         y_axis = abs(coin_position[1] - position[1])

#         num_movements = x_axis + y_axis

#         if num_movements not in movements_to_coins:
#             movements_to_coins[(x_axis + y_axis)] = coin_position

#     shortest_movement = sorted(movements_to_coins)[0]

#     return movements_to_coins[shortest_movement]


## O(n) version


def closest_coin(coins: list, position: tuple):

    shortest_movement = 0
    closest_coin = 0

    for coin_position in coins:

        x_axis = abs(coin_position[0] - position[0])
        y_axis = abs(coin_position[1] - position[1])

        num_movements = x_axis + y_axis

        if num_movements == 0:
            return coin_position
        elif shortest_movement == 0 or num_movements < shortest_movement:
            shortest_movement = num_movements
            closest_coin = coin_position

    return closest_coin


# tests

coins = {
    "test1": [(0, 4), (1, 0), (2, 0), (3, 2)],
    "test2": [(1, 0), (2, 0), (2, 2), (2, 4), (3, 0), (3, 2)],
    "test3": [(1, 0), (2, 0), (2, 2), (2, 4), (3, 0), (3, 2)],
}
positions = {"test1": (0, 2), "test2": (1, 3), "test3": (2, 2)}
correct_result = {"test1": [(0, 4)], "test2": [(2, 2), (2, 4)], "test3": [(2, 2)]}

for test_num in coins:
    result = closest_coin(coins=coins[test_num], position=positions[test_num])
    print(
        f"For {test_num}, where my position is {positions[test_num]} the closest coin in in position {result}"
    )
    assert result in correct_result[test_num]
