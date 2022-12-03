from utils import open_file


def find_the_most_calories(content):
    sum = 0
    max = 0
    results = []
    for row in content:
        if row == '':
            max = max if max > sum else sum
            results.append(sum)
            sum = 0
        else:
            sum += int(row)
    return max, results


def find_top_three_calories(calories):
    calories = sorted(calories, reverse=True)
    return calories[:3]


if __name__ == "__main__":
    data = open_file("calorie_input.txt")
    max, results = find_the_most_calories(data)
    print(max)
    print(sum(find_top_three_calories(results)))
