import numpy as np
import pandas as pd
import os
import json
def new_plant_creator(name, path): 
    print(f"Creating a new file called {name}.xlsx...")
    # print(path)
    dataset_creator(name, path)
    return 0

def dataset_creator(name, path):
    growth_stage = ['Budding Stage', 'Seedling Stage', 'Vegetative Stage',
                    'Flowering Stage', 'Fruit Development', 'Ripe Stage']
    
    temperature_range = []
    humidity_range = []
    light_range = []
    co2_levels = []
    ec_values = []
    ph_values = []
    plant_height_range = []
    leaf_count_range = []

    def format():
        for i in range(10):
            print("-", end=" ")
        print('\n')
    
    def add_values():
    # Prompt the user to enter values for temperature ranges
        for stage in growth_stage:
            min_temp = float(input(f"Enter the minimum temperature for {stage}: "))
            max_temp = float(input(f"Enter the maximum temperature for {stage}: "))
            temperature_range.append([min_temp, max_temp])

        format()
        # Prompt the user to enter values for humidity ranges
        for stage in growth_stage:
            min_humidity = float(input(f"Enter the minimum humidity for {stage}: "))
            max_humidity = float(input(f"Enter the maximum humidity for {stage}: "))
            humidity_range.append([min_humidity, max_humidity])
        format()

        # Prompt the user to enter values for light ranges
        for stage in growth_stage:
            min_light = float(input(f"Enter the minimum light for {stage}: "))
            max_light = float(input(f"Enter the maximum light for {stage}: "))
            light_range.append([min_light, max_light])
        format()

        # Prompt the user to enter values for CO2 levels
        for stage in growth_stage:
            min_co2 = float(input(f"Enter the minimum CO2 level for {stage}: "))
            max_co2 = float(input(f"Enter the maximum CO2 level for {stage}: "))
            co2_levels.append([min_co2, max_co2])
        format()

        # Prompt the user to enter values for EC values
        for stage in growth_stage:
            min_ec = float(input(f"Enter the minimum EC value for {stage}: "))
            max_ec = float(input(f"Enter the maximum EC value for {stage}: "))
            ec_values.append([min_ec, max_ec])
        format()

        # Prompt the user to enter values for pH values
        for stage in growth_stage:
            min_pH = float(input(f"Enter the minimum pH value for {stage}: "))
            max_pH = float(input(f"Enter the maximum pH value for {stage}: "))
            ph_values.append([min_pH, max_pH])
        format()

        # Prompt the user to enter values for plant height ranges
        for stage in growth_stage:
            min_height = float(input(f"Enter the minimum plant height for {stage}: "))
            max_height = float(input(f"Enter the maximum plant height for {stage}: "))
            plant_height_range.append([min_height, max_height])
        format()

        # Prompt the user to enter values for leaf count ranges
        for stage in growth_stage:
            min_leaves = int(input(f"Enter the minimum leaf count for {stage}: "))
            max_leaves = int(input(f"Enter the maximum leaf count for {stage}: "))
            leaf_count_range.append([min_leaves, max_leaves])
        format()

        ranges_data = {
            'temperature_range': temperature_range,
            'humidity_range': humidity_range,
            'light_range': light_range,
            'co2_levels': co2_levels,
            'ec_values': ec_values,
            'ph_values': ph_values,
            'plant_height_range': plant_height_range,
            'leaf_count_range': leaf_count_range
        }

        with open(f'{name}.json', 'w') as file:
            json.dump(ranges_data, file)

    # add_values()
    data = []

    if os.path.exists(f"{name}.json"):
        with open(f'{name}.json','r') as file:
            ranges_data = json.load(file)
        temperature_range = ranges_data['temperature_range']
        humidity_range = ranges_data['humidity_range']
        light_range = ranges_data['light_range']
        co2_levels = ranges_data['co2_levels']
        ec_values = ranges_data['ec_values']
        ph_values = ranges_data['ph_values']
        plant_height_range = ranges_data['plant_height_range']
        leaf_count_range = ranges_data['leaf_count_range']
    else:
        print(f"{name}.json doesnot exist. Creating the file.")
        add_values()

    for i in range(len(growth_stage)):
        temperature = np.random.uniform(temperature_range[i][0], temperature_range[i][1], size=1500)
        humidity = np.random.uniform(humidity_range[i][0], humidity_range[i][1], size=1500)
        light = np.random.uniform(light_range[i][0], light_range[i][1], size=1500) if len(light_range[i]) == 2 else [np.nan] * 1500
        co2 = np.random.uniform(co2_levels[i][0], co2_levels[i][1], size=1500)
        ec = np.random.uniform(ec_values[i][0], ec_values[i][1], size=1500)
        pH = np.random.uniform(ph_values[0][0], ph_values[0][1], size=1500)
        plant_height = np.random.uniform(plant_height_range[i][0], plant_height_range[i][1], size=1500)
        leaf_count = np.random.randint(leaf_count_range[i][0], leaf_count_range[i][1]+1, size=1500)
        stage = [growth_stage[i]] * 1500

        stage_data = list(zip(temperature, humidity, light, co2, ec, pH, plant_height, leaf_count, stage))
        data.extend(stage_data)

    df = pd.DataFrame(data, columns=['temperature', 'humidity', 'light',
                                    'co2', 'ec', 'pH', 'plantheight', 'leafcount', 'stage'])
    df = df.sample(frac=1).reset_index(drop=True)  # Shuffle the dataset

    df.to_excel(path, str(name) + ".xlsx")
    
