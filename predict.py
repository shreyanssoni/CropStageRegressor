import pandas as pd
import os
from data_former import new_plant_creator
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

folder_path = 'C:/Users/soni2/Desktop/Shreyans/AI/Crop/Control/workbooks'

name = []
def select_file():
    file_list = os.listdir(folder_path)
    xlsx = [file for file in file_list if file.endswith('.xlsx')]
    # print(xlsx)
    if xlsx != []:
        print("Following plant models were found: ")
        for i, file in enumerate(xlsx, 1):
            print(f"{i}. {file[:-5]}")
        print(f"{i+1}. Create a new plant.")
        selection = input("Enter the number corresponding to the plant growing: ")
        print("\n")
    else: 
        print("No plant data exists. Creating a new plant. ")
        selection = 1;
    try: 
        selection = int(selection)
        if 1 <= selection <= len(xlsx):
            selected_file = xlsx[selection -1 ]
            print(f"You selected: {selected_file[:-5]}")
            name = selected_file.lower()
            print("reached here")
            if name != None: 
                print(f"reached here also, {name}")
                return name
            else: print("Name not found. Press Ctrl + C to quit.")
        elif selection == len(xlsx) + 1:
            new_plant = input("Enter the name of new plant: ")
            if os.path.exists(folder_path + "/" + new_plant + ".xlsx"):
                print("This file already exists in the folder.\nProceeding to model prediction...")
            else: 
                # Workbook().save(f"{folder_path}/{new_plant}.xlsx")
                path = folder_path + "/" + new_plant + ".xlsx"
                new_plant_creator(new_plant, path)
                print(f"New file called {new_plant}.xlsx created!")
            return str(new_plant) + ".xlsx"
        else: 
            print("...Invalid Selection, Retry!\n")
            select_file()
    except ValueError:
        print("...Invalid input, Retry!\n")
        select_file()

def prediction_model():
    ordinal_encoder = OrdinalEncoder()
    data['stage_encoded'] = ordinal_encoder.fit_transform(data[['stage']])
    print("Label encoding of categorical values done...")

    X = data[['plantheight', 'leafcount']]
    y = data[['stage_encoded','temperature', 'humidity', 'light', 'co2', 'ec', 'pH']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    model = RandomForestRegressor(n_estimators=500, random_state=42,max_depth=10, min_samples_leaf=10, min_samples_split=10)

    model.fit(X_train,y_train)
    print("Model training done...")

    def accuracy():
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        # print("MAE value: ", mae)
        return mae

    # Taking user input for prediction: 

    def user_predictions(): 

        print(f"The MAE of this model is found to be: {accuracy()}")

        height = input("Average of height values: ")
        leafcount = input("Average of Leaf Count: ")
        input_data = pd.DataFrame({'plantheight': [height], 'leafcount': [leafcount]})

        input_data.columns = X.columns
        suggested_conditions = model.predict(input_data)
        print("prediction performed.")
        stage_encoded = round(suggested_conditions[0][0])
        temperature = round(suggested_conditions[0][1], 2) 
        humidity = round(suggested_conditions[0][2],2)        
        light = round(suggested_conditions[0][3], 2)
        co2 = round(suggested_conditions[0][4],2)
        ec = round(suggested_conditions[0][5],2)
        pH = round(suggested_conditions[0][6],2)

        stage = ordinal_encoder.inverse_transform([[stage_encoded]])[0]
        print("decoding categorical values...")
        stagestr = ''.join(stage)
        headers = ["Growth Stage", "Temperature", "Humidity", "Light", "CO2 Levels", "EC", "pH"]

        table_data = [
            [stagestr, temperature, humidity, light, co2, ec, pH]
        ]
        print("printing results...")
        printtable(headers, table_data)

        return 0

    def printtable(headers, table_data):
        column_widths = [max(len(str(item)) for item in col) for col in zip(headers, *table_data)]

        def print_horizontal_line():
            print("+", end="")
            for width in column_widths:
                print("-" * (width + 2), end="+")
            print()

        print_horizontal_line()

        for i, header in enumerate(headers):
            print("\033[2m" + f"| {header:<{column_widths[i]}}" + "\033[0m", end=" ")
        print("|")

        print_horizontal_line()

        for row in table_data:
            for i, item in enumerate(row):
                print(f"| {str(item):<{column_widths[i]}}", end=" ")
            print("|")

        print_horizontal_line()

        return 0

    user_input = input("Press Enter key for User Predictions ")
    if user_input == "": 
        user_predictions()
    else: 
        print("Invalid input key.")

name = select_file()
if name != None: 
    if os.path.exists(folder_path + "/" + str(name)): 
        data = pd.read_excel(folder_path + "/" + str(name))
        prediction_model()
    else: 
        print(f"The file {name} does not exist!") 
else: 
    print("\nCouldn't Capture due to error. Try once again...\n")
    name = select_file()
    data = pd.read_excel(folder_path + "/" + str(name))
    prediction_model()