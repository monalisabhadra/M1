def ai_number_guesser():

    name = input("👋 Hi there! What's your name? ")

    print(f"\nNice to meet you, {name}! 🎉")
    low = int(input(f"{name}, what should be the lowest number I can guess? "))
    high = int(input(f"And what should be the highest number I can guess? "))
    attempts = 0

    print(f"\n🤖 Welcome to the AI Number Guesser, {name}! 🎉")
    print(f"Think of a number between {low} and {high}, and I'll try to guess it! 🧠✨")
    input("🔑 Press Enter when you're ready...")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\n🎯 My guess is: {guess}")
        feedback = input("Press (h) to guess higher 🔼, (l) to guess lower 🔽, or (c) for Correct ✅? ").lower()

        if feedback == 'c' :
            print(f"🎉 Yay! I guessed your number {guess} correctly in {attempts} attempts, {name}! 🏆")
            break
        elif feedback == 'h' :
            low = guess + 1
            print("🔼 Got it! I'll guess higher next time.")
        elif feedback == 'l' :
            high = guess - 1
            print("🔽 Got it! I'll guess lower next time.")
        else:
            print("❗ Please enter 'h' for higher 🔼, 'l' for lower 🔽, or 'c' for correct ✅.")

    if low > high:
        print(f"🤔 Hmm, something went wrong, {name}. Are you sure you followed the rules?")

# Run the AI Number Guesser
ai_number_guesser()

