# CropStageRegressor

CropStageRegressor is a machine learning-based tool that predicts crop growth stages using plant height and leaf count as inputs. It provides insights into the optimal environmental conditions for each growth stage, assisting farmers in optimizing crop growth and ensuring better yields.

## Idea
The CropStageRegressor utilizes a Random Forest regression model to predict the growth stage of crops based on plant height and leaf count. It employs ordinal encoding to handle categorical values and provides recommendations for temperature, humidity, light, CO2 levels, EC, and pH suitable for each growth stage. The tool allows users to input average plant height and leaf count, and it returns the predicted growth stage and corresponding optimal environmental conditions.

## Usage
1. Ensure your dataset is in the proper format, including plant height, leaf count, and growth stage information.
2. Use the data_former module to generate datasets within the desired ranges.
3. Run predict.py to start the application.
4. Select the plant model or create a new plant if no data exists.
5. Input the average plant height and leaf count.
6. Receive the predicted growth stage and optimal environmental conditions.
7. Utilize the recommendations to optimize crop growth and adjust environmental factors accordingly.

**Important Note: Create a folder called "workbooks" in the directory for datasets to be saved.**
---

To run the code, execute the following command:

```shell
python predict.py



