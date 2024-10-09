from rich.console import Console
from rich.table import Table
import json
import os

# Create a Console instance
console = Console()
console.print("Here is some initial data:", style="bold cyan")
table = Table(title="Popular Video Games")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Genre", style="green")
table.add_row("Nov 10, 2020", "Assassin's Creed Valhalla", "Action RPG")
table.add_row("Dec 10, 2020", "Cyberpunk 2077", "Action RPG")
table.add_row("Sep 4, 2020", "Marvel's Avengers", "Action-adventure")
table.add_row("Mar 20, 2020", "Animal Crossing: New Horizons", "Simulation")
console.print(table)
console.print("\n[bold cyan]Now I want you to enter your preferred video games:[/bold cyan]")

def get_user_data():
    game_title = console.input("Enter the title of the game: ")
    release_date = console.input("Enter the release date of the game: ")
    genre = console.input("Enter the genre of the game: ")
    return {
        "title": game_title,
        "release_date": release_date,
        "genre": genre
    }


games = []
while True:
    game = get_user_data()
    console.print("\n[bold yellow]You entered the following data:[/bold yellow]")
    console.print(f"Title: {game['title']}")
    console.print(f"Release Date: {game['release_date']}")
    console.print(f"Genre: {game['genre']}")
    
    confirm = console.input("\nIs this data correct? (yes/no): ").strip().lower()
    if confirm == 'yes':
        games.append(game)
        another = console.input("Do you want to enter another game? (yes/no): ").strip().lower()
        if another != 'yes':
            break
    else:
        console.print("[bold red]Please re-enter the data.[/bold red]")

# Save the data to a file
file_path = os.path.join(os.getcwd(), "games.json")
with open(file_path, 'w') as file:
    json.dump(games, file, indent=4)

console.print(f"\n[bold green]Data has been saved to {file_path}[/bold green]")