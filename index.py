import math
import numpy as np
import psycopg2
import random
from collections import Counter

bincom_staffs_dress_colors = {
  "Monday":["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
  "Tuesday":["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
  "Wednesday":["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
  "Thursday":["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
  "Friday":["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]}

all_colors = []

def get_all_colors(bincom_staffs_dress_colors):
  for color in bincom_staffs_dress_colors:
    all_colors.extend(bincom_staffs_dress_colors[color])

  return all_colors

get_all_colors(bincom_staffs_dress_colors)

def get_mean_color(all_colors):
  mean_color = {}
  for color in all_colors:
    mean_color[color] = all_colors.count(color)
  
  val_sum = 0

  for val in mean_color.values():
    val_sum += val
  
  mean_val = val_sum / len(mean_color)

  mean_color = all_colors[math.floor(mean_val)]

  return (mean_color)

print(f"{get_mean_color(all_colors)} is the mean color")

def get_mode_color(all_colors):
  all_color = {}
  for color in all_colors:
    all_color[color] = all_colors.count(color)
  
  mode_color = max(all_color, key=all_color.get)

  return mode_color

print(f"{get_mode_color(all_colors)} is mostly worn throughout the week")

def get_median_color(all_colors):
  median_pos = math.floor(len(all_colors) / 2) + 1

  all_colors = sorted(all_colors)

  median = all_colors[median_pos]

  return median

print(f"{get_median_color(all_colors)} is the median")

def get_variance(all_colors):
  color_mapping = {color: index for index, color in enumerate(set(all_colors))}
  numeric_colors = [color_mapping[color] for color in all_colors]
  variance = np.var(numeric_colors)

  return variance

print(f"{get_variance(all_colors)} is the variance of the colors")


#Save in POSTGRES Database

# Count occurrences of each color
color_counts = Counter(sorted(all_colors))

# Connect to PostgreSQL database
conn = psycopg2.connect('postgres://avnadmin:AVNS_jpmUuPitB70G-fNOio1@colorsdb-colors-db.a.aivencloud.com:28750/defaultdb?sslmode=require')

# Create a cursor object
cur = conn.cursor()

# Create a table to store colors and frequencies
cur.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(50) PRIMARY KEY,
        frequency INT
    )
""")

# Insert colors and frequencies into the database
for color, frequency in color_counts.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s) ON CONFLICT (color) DO NOTHING", (color, frequency))


# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

def random_number_generator():
    digits = [0, 1]
    random_number = random.choice(digits)
    return random_number

def random_base2_number_generator():
    base2_num = ""
    for i in range(4):  # Generate four random digits
        base2_num += str(random_number_generator())
    return base2_num

def base2_to_base10(base2_num):
    base10_num = 0
    i = len(base2_num) - 1
    j = 0
    while i >= 0:
        base10_num += int(base2_num[j]) * (2 ** i)
        i -= 1
        j += 1
    return base10_num

base2_num = random_base2_number_generator()

print(f"The Base-10 Equivalent of the Random Base-2 Number: {base2_num} is {base2_to_base10(base2_num)}")


def fib_sum():
    a = 1
    b = 1
    fib_sum = 0

    for i in range(50):
        fib_sum += a
        c = a + b
        a = b
        b = c

    return fib_sum

print("The Sum of the first 50 Fibonacci numbers:", fib_sum())