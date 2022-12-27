import random
import datetime

random.seed(0)
INSERT_STATEMENT = "INSERT INTO event_db.event_tab(title, description, start_time, end_time, category, location) VALUES ('{title}', '{description}', '{start_time}', '{end_time}', '{category}', '{location}');"
LOCATIONS = ["Singapore", "Malaysia", "Indonesia", "America", "Japan", "Korea", "Australia", "Brazil", "Mexico", "Argentina", "Spain", "Germany"]
START_YEARS = [2020, 2021, 2022]
END_YEARS = [2022, 2023, 2024]


def main():
    with open("sample_data.sql", "w") as f:
        for i in range(1000000):
            start_time = datetime.datetime(random.choice(START_YEARS), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59))
            end_time = datetime.datetime(random.choice(END_YEARS), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59))
            f.write(INSERT_STATEMENT.format(title="TITLE_" + str(i), description="DESCRIPTION_" + str(i),
                                            start_time=str(start_time), end_time=str(end_time),
                                            category="CATEGORY_" + str(random.randint(1, 10)), location=random.choice(LOCATIONS)))
            f.write("\n")

if __name__ == "__main__":
    main()