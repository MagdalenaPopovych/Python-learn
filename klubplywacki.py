import statistics

FOLDER = "daneztreningow/"


def read_swim_data(filename):

    # Zwraca czasy z pliku 
    # Na podstawie nazwy pliku pływaka funkcja pobiera dane ze wskazanego pliku i zwraca je w formach krotki

    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(";")

    converts = []

    for t in times:
        
        # Może brakować wartości minut, musimy się przed tym zabezpieczyć

        if ":" in t:
            minutes, rest = t.split(":")
            seconds, hundredths = rest.split(",")
        else:
            minutes = 0
            seconds, hundredths - t.split(",") 
        converts.append((int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths))

    avarage = statistics.mean(converts)
    mins_secs, hundredths = str(round(avarage / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    avarage = f"{minutes}:{seconds},{hundredths}"

    return swimmer, age, distance, stroke, times, avarage, converts


