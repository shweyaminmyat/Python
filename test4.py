# answer = input("""Enter Weather (Sunny, Rainy, Windy)""")
# if answer == "Sunny":
#     print("The weather is too good to be sad.")
# elif answer == "Rainy":
#     print("雨过天晴")
# elif answer == "Windy":
#     print("let me go with the wind")
# else:
#     print("Enter Weather (Sunny, Rainy, Windy)")

answer = input("""Enter music type (Rock, classical, Pop)""")
if answer == "Rock":
    artist_ques = input("Do you like Bon Jovi? (y/n)")
    if artist_ques == 'y':
        print("Me too")
    if artist_ques == 'n':
        print("I recommend you to listen his famous song, It's my life")
elif answer == "Classical":
    print("Good choice")
elif answer =="Pop":
    print("Ok")
else: print("Just answer within three")