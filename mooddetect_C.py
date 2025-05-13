# Import necessary libraries
import colorama
from colorama import Fore, Style
from textblob import TextBlob
# - TextBlob for natural language processing tasks like sentiment analysis
# - Colorama for colored terminal output
# - sys and time for animations and delays
user_name = input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}").strip()

if not user_name:

    user_name = "Mystery Agent" # Fallback if user doesn’t provide a name
conversation_history = []
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")

print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. 🔍")

print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "f"or {Fore.YELLOW}’exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:

    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:

        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":

        print(f"\n{Fore.BLUE}🚪 Exiting Sentiment Spy. Farewell, Agent {user_name}! 🏁{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":

        conversation_history.clear()

        print(f"{Fore.CYAN}🎉 All conversation history cleared!{Style.RESET_ALL}")

        continue    
    elif user_input.lower() == "history":

         if not conversation_history:

            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")

         else:

            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):

             if sentiment_type == "Positive":

                color = Fore.GREEN

                emoji = "😊"

             elif sentiment_type == "Negative":

                color = Fore.RED

                emoji = "😢"

             else:

                color = Fore.YELLOW

                emoji = "😐"

             print(f"{idx}. {color}{emoji} {text} "

                  f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")

         continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:

     sentiment_type = "Positive"

     color = Fore.GREEN

     emoji = "😊"

    elif polarity < -0.25:
        sentiment_type = "Negative"

        color = Fore.RED

        emoji = "😢"

    else:

        sentiment_type = "Neutral"

        color = Fore.YELLOW

        emoji = "😐"

conversation_history.append((user_input, polarity, sentiment_type))

print(f"{color}{emoji} {sentiment_type} sentiment detected! "

      f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")    
# Initialize Colorama to reset terminal colors automatically after each output

# Define global variables
# - `user_name`: To store the name of the user (Agent)
# - `conversation_history`: A list to store all user inputs
# - Sentiment counters (`positive_count`, `negative_count`, `neutral_count`) to track sentiment trends

# Define a function to simulate a processing animation
# - Prints "loading dots" to make the chatbot feel interactive
# - Use a loop to display three dots with a slight delay

# Define a function to analyze sentiment of the text
# - Use TextBlob to calculate the polarity of the input text
# - Categorize the sentiment into "Very Positive," "Positive," "Neutral," "Negative," or "Very Negative"
# - Append the user input to `conversation_history`
# - Update the sentiment counters based on the category
# - Handle exceptions to avoid crashes

# Define a function to handle commands
# - Handle commands like `summary`, `reset`, `history`, and `help`
# - `summary`: Displays the count of positive, negative, and neutral sentiments
# - `reset`: Clears the conversation history and resets counters
# - `history`: Shows all previous user inputs
# - `help`: Displays a list of available commands
# - Return appropriate responses for each command

# Define a function to validate the user's name
# - Continuously prompt the user for a name until they enter a valid alphabetic string
# - Strip any extra spaces and ensure the input is not empty or invalid

# Define the main function to start the chatbot
# - Display a welcome message and introduce the Sentiment Spy activity
# - Ask the user for their name and store it in the `user_name` variable
# - Enter an infinite loop to interact with the user:
#   - Prompt the user to enter a sentence or command
#   - Check for empty input and prompt the user to enter a valid sentence
#   - If the input matches specific commands (`exit`, `summary`, `reset`, `history`, `help`), execute the corresponding functionality
#   - Otherwise, call the `analyze_sentiment` function to analyze the input text
#   - Display the sentiment analysis result with color-coded feedback
# - Exit the loop and display a final summary when the user types `exit`

# Define the entry point for the script
# - Ensure the chatbot starts only when the script is run directly (not imported)
# - Call the `start_sentiment_chat` function to begin the activity
