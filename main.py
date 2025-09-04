import random
print("Welcome to the emoji fortune teller!🎱")
name = input("What is your name? ")
print("Hello, " + name + "! Let's see your fortune...")

fortunes = [
  "🌟 " + name + " will have an amazing day!",
  "🍕Pizza is in " + name + "'s future.",
  "🎁A surprise is waiting for " + name + " soon.",
  "🐶A new furry friend will bring " + name + " joy.",
  "🚀Adventure is on the horizon for " + name + "!",
  "💸" + name + "  will gain a lot of wealth in their future.",
  "🥳There is a lot of fun in " + name + "'s future.",
  "🍦A sweet treat is on the horizon for " + name,
  "🛫A relaxing vacation is close in " + name + "'s future.",
  "😱" + name + " got the only bad fortune! Something unlucky is in their future...",
  "😴Zzz... Oh! " + name + " woke the emoji fortune teller up!"
]

choice = input("Would you like to see your fortune?(yes/no) ")
while choice == "yes":
  fortune = random.choice(fortunes)
  print("Your fortune is: " + fortune)
  choice = input("Would you like to see another one of your fortunes?(yes/no) ")

if choice != "yes":
  print("Thanks for playing with the Emoji Fortune Teller!")