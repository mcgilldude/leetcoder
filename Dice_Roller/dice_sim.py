import random
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

def roll_dice(num_dice, num_rolls):
    results = []
    for _ in range(num_rolls):
        dice_values = [random.randint(1, 6) for _ in range(num_dice)]
        results.append(dice_values)
    return results

def plot_average(results):
    averages = [statistics.mean(rolls) for rolls in zip(*results)]
    colors = sns.color_palette('viridis', n_colors=len(averages))
    plt.bar(range(1, len(averages) + 1), averages, color=colors)
    plt.xlabel('Dice')
    plt.ylabel('Average of Dice Rolls')
    plt.title('Average Dice Rolls for Each Die')
    plt.show()

def main():
    print("Welcome to the Dice Rolling Simulator!")

    try:
        num_dice = int(input("Enter the number of dice: "))
        num_rolls = int(input("Enter the number of rolls: "))
        
        if num_dice <= 0 or num_rolls <= 0:
            print("Please enter valid positive numbers for dice and rolls.")
        else:
            dice_results = roll_dice(num_dice, num_rolls)

            print(f"\nResults of rolling {num_dice} dice {num_rolls} times:")
            for i, rolls in enumerate(dice_results, start=1):
                print(f"Roll {i}: {rolls}")

            # Plot average for each die
            plot_average(dice_results)

    except ValueError:
        print("Please enter valid integers for dice and rolls.")

if __name__ == "__main__":
    main()
