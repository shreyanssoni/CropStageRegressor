CropStageRegressor

CropStageRegressor is a machine learning-based tool that predicts crop growth stages using plant height and leaf count as inputs. It provides insights into the optimal environmental conditions for each growth stage, assisting farmers in optimizing crop growth and ensuring better yields.

Idea
The CropStageRegressor utilizes a Random Forest regression model to predict the growth stage of crops based on plant height and leaf count. It employs the concept of ordinal encoding to handle categorical values and provides recommendations for temperature, humidity, light, CO2 levels, EC, and pH suitable for each growth stage. The tool allows users to input average plant height and leaf count, and it returns the predicted growth stage and corresponding optimal environmental conditions.

Usage
Ensure your dataset is in the proper format, including plant height, leaf count, and growth stage information.
The data_former module generates the datasets within the desired ranges.
Run predict.py to start the application.
Select the plant model or create a new plant if no data exists.
Input the average plant height and leaf count.
Receive the predicted growth stage and optimal environmental conditions.
Utilize the recommendations to optimize crop growth and adjust environmental factors accordingly.