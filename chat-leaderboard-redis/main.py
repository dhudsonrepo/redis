from chat.chat_client import ChatClient
from leaderboard.leaderboard import Leaderboard

def main():
    # Chat system setup
    username = input("Enter your chat username: ")
    chat_client = ChatClient(username)

    # Leaderboard setup
    leaderboard = Leaderboard()

    while True:
        print("\n1. Send a message")
        print("2. View leaderboard")
        print("3. Add score")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter message: ")
            chat_client.send_message(message)

        elif choice == "2":
            top_scores = leaderboard.get_top_scores()
            print("\nLeaderboard:")
            for rank, (username, score) in enumerate(top_scores, start=1):
                print(f"{rank}. {username.decode('utf-8')} - {score}")

        elif choice == "3":
            score = int(input("Enter score to add: "))
            leaderboard.add_score(username, score)
            print(f"Score added for {username}")

        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
