from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.table import Table
from rich.console import Console
import requests
from player import Player

def main():
    console = Console()

    season = console.input("Season [purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/purple] [light_blue](2024-25)[/light_blue]") or "2024-25"
    reader = PlayerReader(season)
    stats = PlayerStats(reader)

    while True:
        country = console.input("Nationality [purple][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/purple]")
        if not country or country in ("QUIT", "EXIT"):
                console.print("\n[bold red]Exiting... Goodbye![/bold red]")
                break
        players = stats.top_scorers_by_nationality(country)
                

        if not players:
            console.print(f"No players found for nationality {country}", style="bold red")
            return    

        table = Table(title=f"Season {season} players from {country}")
        table.add_column("Released", style="cyan", no_wrap=True)
        table.add_column("teams", style="purple")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for p in players:
            teams = ", ".join(p.team) if isinstance(p.team, list) else p.team
            table.add_row(p.name, teams, str(p.goals), str(p.assists), str(p.points))

        console.print(table)
        console.print("")


main()

