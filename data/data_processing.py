# import pandas as pd
# import os
# from sklearn.preprocessing import MinMaxScaler


# def clean_and_preprocess_data(filepath, output_path):
#     # Specify the columns to keep
#     columns_of_interest = ['date', 'avg_hourly_temperature', 'precipitation', 'avg_hourly_pressure_station', 'solar_radiation']
    
#     # Load the data
#     data = pd.read_csv(filepath, usecols=columns_of_interest)
#     data['date'] = pd.to_datetime(data['date'])
    
#     # Interpolate missing solar radiation values
#     data['solar_radiation'].interpolate(method='linear', inplace=True)
    
#     # Filter data for May 1st to November 30th for each year
#     data = data[(data['date'].dt.month >= 5) & (data['date'].dt.month <= 11)]
    
#     # Drop rows where any of the required columns are missing
#     # data = data.dropna()

#     if not data.empty:
#         # Scale the data
#         scaler = MinMaxScaler(feature_range=(0, 1))
#         data_scaled = pd.DataFrame(scaler.fit_transform(data[columns_of_interest[1:]]), columns=columns_of_interest[1:])
#         data_scaled['date'] = data['date'].values  # Append the date back to the scaled data
        
#         # Save the cleaned and scaled data to a new file
#         output_file = os.path.join(output_path, os.path.basename(filepath))
#         data_scaled.to_csv(output_file, index=False)
#         print(f"Processed and saved: {output_file}")
#     else:
#         print(f"No data to process after filtering for {filepath}")

# def process_all_csv(input_directory, output_directory):
#     # Ensure output directory exists
#     os.makedirs(output_directory, exist_ok=True)
    
#     # List all files in the input directory
#     files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]
    
#     # Process each file
#     for file in files:
#         file_path = os.path.join(input_directory, file)
#         clean_and_preprocess_data(file_path, output_directory)

# if __name__=="__main__":
#     # Set the paths
#     input_directory = "data/raw"
#     output_directory = "data/formated"

#     # Process all CSV files in the directory
#     process_all_csv(input_directory, output_directory)

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os


def preprocess_and_save_data(file_name, base_url, output_directory):
    # Construct the full URL
    url = f"{base_url}/{file_name}"
    print(url)
    
    # Load the data
    data = pd.read_csv(url)
    data['date'] = pd.to_datetime(data['date'])
    
    # Interpolate missing solar radiation values
    data['solar_radiation'].interpolate(method='linear', inplace=True)
    
    # Filter data for dates between May 1st and November 30th, between 2015 and 2022
    data = data[(data['date'].dt.month >= 5) & (data['date'].dt.month <= 11)]
    data = data[(data['date'].dt.year >= 2015) & (data['date'].dt.year <= 2022)]
    
    # Select the required columns and drop rows with missing data
    columns_required = ['date', 'avg_hourly_temperature', 'precipitation', 'avg_hourly_pressure_station', 'solar_radiation']
    data = data[columns_required].dropna()
    
    # Scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled_values = scaler.fit_transform(data[columns_required[1:]])
    data_scaled = pd.DataFrame(data_scaled_values, columns=columns_required[1:])
    data_scaled.insert(0, 'date', data['date'].values)
    
    # Save the cleaned and scaled data to a new file
    output_file = os.path.join(output_directory, os.path.splitext(file_name)[0] + '_processed.csv')
    data_scaled.to_csv(output_file, index=False)
    print(f"Processed and saved: {output_file}")

if __name__ == "__main__":
    base_url = 'https://raw.githubusercontent.com/noobstang/NNtraining/master/Weather49Sets'
    output_directory = "data/formated"
    file_names = [
        'weatherstats_ottawa_daily.csv',
        'weatherstats_chelsea_daily.csv',
        'weatherstats_gatineau_daily.csv',
        'weatherstats_kemptville_daily.csv',
        'weatherstats_ottawasouth_daily.csv',
        'weatherstats_renfrew_daily.csv'
    ]

    for file_name in file_names:
        preprocess_and_save_data(file_name, base_url, output_directory)
