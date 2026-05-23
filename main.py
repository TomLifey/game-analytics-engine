def get_data():
    return [
        ["Minecraft", "Sandbox", 2011],
        ["Valorant", "Shooter", 2020],
        ["Terraria", "Sandbox", 2011],
        ["Roblox", "Sandbox", 2006],
        ["Fortnite", "Shooter", 2017],
        ["The Witcher 3", "RPG", 2015],
        ["Elden Ring", "RPG", 2022],
        ["Stardew Valley", "RPG", 2016],
        ["Skyrim", "RPG", 2011],
        ["Starcraft II", "Strategy", 2010],
        ["Civilization VI", "Strategy", 2016],
        ["Apex Legends", "Shooter", 2019],
        ["Rust", "Survival", 2013],
        ["Subnautica", "Survival", 2014],
        ["Portal 2", "Puzzle", 2011],
        ["Tetris Effect", "Puzzle", 2018],
        ["Resident Evil Village", "Horror", 2021],
        ["Dead Space", "Horror", 2008],
        ["FIFA 23", "Sports", 2022],
        ["Rocket League", "Sports", 2015],
        ["Overwatch 2", "Shooter", 2022],
        ["Hollow Knight", "RPG", 2017],
        ["Dota 2", "Strategy", 2013]
    ]

def get_summary(data):
    counts = {}
    for row in data:
        genre = row[1]
        counts[genre] = counts.get(genre, 0) + 1
    return counts

def main():
    data = get_data()
    print("=============================================")
    print("      ADVANCED GAME ANALYTICS ENGINE")
    print("=============================================")
    
    while True:
        summary = get_summary(data)
        # Display available genres nicely
        print("\nAvailable Categories:", ", ".join(summary.keys()))
        
        # Take input and immediately convert to lowercase for internal processing
        user_input = input("\nEnter a genre to search (or 'quit'): ").strip().lower()
        
        if user_input == 'quit':
            print("\nShutting down Analytics Engine. Goodbye!")
            break
        
        # Filter Logic: Compare everything in lowercase!
        # This makes 'RPG', 'rPg', and 'rpg' all equal to 'rpg'
        results = [row for row in data if row[1].lower() == user_input]
        
        # Sort results by release year
        sorted_results = sorted(results, key=lambda x: x[2])
        
        if sorted_results:
            # Capitalize the output for a clean, professional look
            print(f"\nFound {len(sorted_results)} game(s) in '{user_input.capitalize()}':")
            for item in sorted_results:
                print(f" -> {item[0]} ({item[2]})")
            
            percentage = (len(sorted_results) / len(data)) * 100
            print(f"\n[Analytics: This category is {percentage:.1f}% of the library]")
        else:
            print(f"Sorry, no games found for '{user_input}'.")
        
        print("\n" + "=" * 45)

if __name__ == "__main__":
    main()
