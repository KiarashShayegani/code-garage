# Q20 practice fixture — data and requirements only
# Do not modify this fixture while implementing your pipeline.

q20_raw_records = [
    {"name": "  Alice  ", "age": "30", "status": "active", "team": "ML"},
    {"name": "Bob", "age": 17, "status": "active", "team": "Data"},
    {"name": "  carol", "age": " 25 ", "status": "inactive", "team": "ML"},
    {"name": "   ", "age": "44", "status": "active", "team": "Data"},
    {"name": "Drew", "age": None, "status": "active", "team": "ML"},
    {"name": "Eve", "age": 25, "status": "paused", "team": "Data"},
    {"name": "Frank", "age": -3, "status": "active", "team": "ML"},
    {"name": "Grace", "age": "not-a-number", "status": "active", "team": "Data"},
    {"name": "Henry", "age": 40, "team": "ML"},
    "malformed row: this is not a dictionary",
    {"name": " Ivy ", "age": 22, "status": "active", "team": "Data", "extra": "keep"},
]

q20_config = {
    "required_fields": ("name", "age"),
    "minimum_age": 18,
    "required_status_for_output": "active",
}

import copy

def normalizer(dataset: list[dict]):
    """
    This function normalizes a dataset
    """
    print("\n---Entering normalizer function:")
    normal_dataset = []
    for row in dataset:
        if isinstance(row, dict):
            for key, value in row.items():
                if isinstance(value, str):
                    row[key] = value.strip()
            normal_dataset.append(row)
    for row in normal_dataset:
        if not isinstance(row.get("age"), int):
            try:
                row["age"] = int(row.get("age"))
            except:
                row["age"] = None
    
    return normal_dataset

def validator(dataset: list[dict], required_fields: tuple):
    print("\n---Entering validator function:")
    # filtered_data = []
    for i, row in enumerate(dataset):
        for rf in required_fields:
            if (row[rf] == None):
                dataset.remove(row)
                print(f"Removed row no.{i} due to not having required fields")
        if len(row["name"]) < 1:
            dataset.remove(row)
            print(f"Removed row no.{i} due to empty name")
        if (not isinstance(row["age"], int) or row["age"] < 0):
            print(f"Removed row no.{i} due to invalid age")
            dataset.remove(row)
    return dataset
    
def filterer(dataset: list[dict], minimum_age: int, required_status_for_output: str) -> list[dict]:
    """
    This function does the remainin filtering based on
    minimum age and status feature of the dataset
    """
    print("\n---Entering filterer function:")
    for i, row in enumerate(dataset):
        # if not isinstance(row.get('age'), int) or row.get('age') == None:
        #     dataset.remove(row)
        if (isinstance(row.get('age'), int) and row.get('age') < minimum_age):
            dataset.remove(row)
            print(f"Removed row no.{i} due to invalid age")
        if (row.get('status') != required_status_for_output):
            dataset.remove(row)
            print(f"Removed row no.{i} due to invalid status")
    return dataset

def summarize(dataset: list[dict], raw_rows, norm_rows, vali_rows, filter_rows) -> dict:
    stats = dict()

    total = 0
    sums = 0
    unique_teams = []
    norm_removed = raw_rows - norm_rows
    vali_removed = norm_rows - vali_rows
    filter_removed = vali_rows - filter_rows
    valid_rows = filter_rows
    for row in dataset:
        if row.get('age') != None:
            sums += row.get('age')
            total += 1
    average_age = sums / total
    for row in dataset:
        unique_teams.append(row.get('team'))
    unique_teams = set(unique_teams)
    team_stats = {team: 0 for team in unique_teams}
    for team in unique_teams:
        for row in dataset:
            if row.get('team') == team:
                team_stats[team] += 1
    stats["input_records"] = raw_rows
    stats["valid_rows"] = valid_rows
    stats["invalid_rows"] = raw_rows - valid_rows
    stats["normalizer_removed"] = norm_removed
    stats["validator_removed"] = vali_removed
    stats["filterer_removed"] = filter_removed
    stats["unique_teams"] = unique_teams
    stats["team_stats"] = team_stats

    return stats


def small_preprocesser(data: list[dict], configs: dict):
    """
    This function acts as a simple data preprocesser
    """
    dataset = copy.deepcopy(data)
    required_fields = configs.get("required_fields")
    minimum_age = configs.get("minimum_age")
    required_status_for_output = configs.get("required_status_for_output")

    if not isinstance(dataset, list):
        raise TypeError("The data must be a dictionary")
    if not isinstance(configs, dict):
        raise TypeError("The configs must be a dictionary")

    raw_rows = len(dataset)
    dataset = normalizer(dataset)
    norm_rows = len(dataset)
    dataset = validator(dataset, required_fields)
    vali_rows = len(dataset)
    dataset = filterer(dataset, minimum_age, required_status_for_output)
    filter_rows = len(dataset)

    analysis = summarize(dataset, raw_rows, norm_rows, vali_rows, filter_rows)

    return dataset, analysis
    
data, stats = small_preprocesser(q20_raw_records, q20_config)
print('-'*50)
print("=== THE DATA ===")
print(data)

print("=== THE STATS ===")
print(stats)

