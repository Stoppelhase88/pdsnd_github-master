## Udacity projekt "Introduction to Python" - Andreas Tusche -> here used for version control learning

import os
import time
import pandas as pd

CITY_FILES = {
    "chicago": "chicago.csv",
    "new york": "new_york_city.csv",
    "washington": "washington.csv"
}

MONTHS = ["january", "february", "march", "april", "may", "june"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# Verzeichnis der CSV-Dateien (relativ zum Skript)
DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def get_valid_input(prompt, valid_options):
    """Keeps asking the user until a valid input is made.

    Args:
        prompt (str): Eingabeaufforderung.
        valid_options (list): List of valid inputs.

    Returns:
        str: Valid User input (lowercase).
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"  Ungültige Eingabe! Erlaubt: {', '.join(valid_options)}")


def format_duration(seconds):
    """Converts seconds to a readable format (days, hours, minutes, seconds).

    Args:
        seconds (float): Duration in sec.

    Returns:
        str: Formatted duration.
    """
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, secs = divmod(remainder, 60)
    parts = []
    if days:
        parts.append(f"{days} Tag(e)")
    if hours:
        parts.append(f"{hours} Std.")
    if minutes:
        parts.append(f"{minutes} Min.")
    parts.append(f"{secs} Sek.")
    return ", ".join(parts)


def load_data(city, month, day):
    """Loads the CSV data and filters by month and day of the week.

    Args:
        city (str): Name der Stadt.
        month (str): Monatsname oder 'all'.
        day (str): Wochentag oder 'all'.

    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    filepath = os.path.join(DATA_DIR, CITY_FILES[city])
    df = pd.read_csv(filepath)

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Weekday"] = df["Start Time"].dt.day_name()
    df["Hour"] = df["Start Time"].dt.hour

    if month != "all":
        month_index = MONTHS.index(month) + 1
        df = df[df["Month"] == month_index]

    if day != "all":
        df = df[df["Weekday"].str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent travel time."""
    print("\n -> Zeit-Statistiken:")
    start = time.time()

    if df.empty:
        print("  Keine Daten für die gewählten Filter vorhanden.")
    else:
        print("• Häufigster Monat:", df["Month"].mode()[0])
        print("• Häufigster Wochentag:", df["Weekday"].mode()[0])
        print("• Häufigste Startstunde:", df["Hour"].mode()[0])

    print(f"  (Berechnung in {time.time() - start:.4f} Sek.)")


def station_stats(df):
    """Displays statistics on the most popular stops and trips."""
    print("\n -> Stations-Statistiken:")
    start = time.time()

    if df.empty:
        print("  Keine Daten für die gewählten Filter vorhanden.")
    else:
        print("• Beliebteste Startstation:", df["Start Station"].mode()[0])
        print("• Beliebteste Endstation:", df["End Station"].mode()[0])

        kombination = df["Start Station"] + " → " + df["End Station"]
        print("• Häufigste Trip-Kombination:", kombination.mode()[0])

    print(f"  (Berechnung in {time.time() - start:.4f} Sek.)")


def trip_duration_stats(df):
    """Displays statistics on the total duration and average duration of trips."""
    print("\n -> Fahrzeit-Statistiken:")
    start = time.time()

    if df.empty:
        print("  Keine Daten für die gewählten Filter vorhanden.")
    else:
        total = df["Trip Duration"].sum()
        avg = df["Trip Duration"].mean()
        print(f"• Gesamtdauer: {format_duration(total)}")
        print(f"• Durchschnittliche Dauer: {format_duration(avg)}")

    print(f"  (Berechnung in {time.time() - start:.4f} Sek.)")


def user_stats(df):
    """Displays statistics about the users (Typen, Geschlecht, Geburtsjahr)."""
    print("\n -> Nutzer-Statistiken:")
    start = time.time()

    if df.empty:
        print("  Keine Daten für die gewählten Filter vorhanden.")
    else:
        print("• Nutzer-Typen:")
        print(df["User Type"].value_counts().to_string(header=False))

        if "Gender" in df.columns:
            print("\n• Geschlechter:")
            print(df["Gender"].value_counts().to_string(header=False))

        if "Birth Year" in df.columns:
            print("\n• Geburtsjahre:")
            print("  Ältester:", int(df["Birth Year"].min()))
            print("  Jüngster:", int(df["Birth Year"].max()))
            print("  Häufigstes:", int(df["Birth Year"].mode()[0]))

    print(f"  (Berechnung in {time.time() - start:.4f} Sek.)")


def show_raw_data(df):
    """If desired, displays 5 rows of raw data each."""
    index = 0
    total = len(df)
    while index < total:
        show = input(f"\nRohdaten anzeigen? ({index}/{total} angezeigt) (ja/nein): ").strip().lower()
        if show != "ja":
            break
        print(df.iloc[index:index + 5].to_string())
        index += 5
    if index >= total:
        print("  Alle Rohdaten wurden angezeigt.")


def main():
    """Main program: Interactive Bikeshare data analysis."""
    while True:
        print("\n=== US Bikeshare Analyse ===")

        city = get_valid_input(
            "Stadt (chicago, new york, washington): ",
            list(CITY_FILES.keys())
        )
        month = get_valid_input(
            "Monat (january–june oder 'all'): ",
            MONTHS + ["all"]
        )
        day = get_valid_input(
            "Wochentag (monday–sunday oder 'all'): ",
            DAYS + ["all"]
        )

        print(f"\nLade Daten für {city.title()}, Monat={month}, Tag={day} ...")
        df = load_data(city, month, day)
        print(f"  {len(df)} Datensätze geladen.")

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input("\nNeu starten? (ja/nein): ").strip().lower()
        if restart != "ja":
            break


if __name__ == "__main__":
    main()
