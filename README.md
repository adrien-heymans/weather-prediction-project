
# Weather Prediction Project

This repository contains the implementation of a weather prediction model for microclimate forecasting, specifically focused on the Ottawa region. The project includes data exploration, model building, and results visualization.

## Project Structure

1. **Data Exploration**
2. **Weather Prediction Models**
3. **Results Plots**

## Prerequisites

Before running the notebooks, ensure you have the following libraries installed:

- `numpy`
- `pandas`
- `matplotlib`
- `tensorflow`
- `scikit-learn`
- `keras-tuner`

You can install these libraries using pip:

```bash
pip install numpy pandas matplotlib tensorflow scikit-learn keras-tuner
```

## Data Exploration

The first step in the project involves exploring the dataset to understand the structure and the relationships between different weather parameters. It is crucial to select the correct column names for the dataset during this step.

### Notebook: `CSI6900 - Data Exploration.ipynb`

This notebook covers:
- Loading the dataset
- Handling missing values
- Generating various plots to visualize the data

## Weather Prediction Models

The second step involves building and training the weather prediction models. The project includes implementations of Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks.

### Notebook: `CSI6900 - Weather Prediction Models.ipynb`

This notebook covers:
- Preprocessing the data
- Building the models
- Training the models with various configurations

### Configurable Settings

The following settings can be changed by the user:
- `n_past`: Number of past time steps to consider for predictions
- `n_future`: Number of future time steps to predict
- `batch_size`: Batch size for training
- `hyper_tuning`: Flag to enable or disable hyperparameter tuning

## Results Plots

The final step involves visualizing the results of the trained models to evaluate their performance. The user must specify the correct directory where the results and plots will be saved.

### Notebook: `CSI6900 - Results Plots.ipynb`

This notebook covers:
- Loading the trained models
- Generating plots to compare the actual and predicted values
- Evaluating the performance of the models

## Usage Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/adrien-heymans/weather-prediction-project.git
    cd weather-prediction-project
    ```

2. **Run Data Exploration Notebook**
    Open and run `CSI6900 - Data Exploration.ipynb` to explore the dataset and generate initial visualizations.

3. **Run Weather Prediction Models Notebook**
    Open and run `CSI6900 - Weather Prediction Models.ipynb` to preprocess the data, build, and train the prediction models. Adjust the configurable settings as needed.

4. **Run Results Plots Notebook**
    Open and run `CSI6900 - Results Plots.ipynb` to visualize the model's performance. Ensure the correct directory is specified for saving the plots.

## Important Notes

- Ensure that the correct directory is specified for saving results and plots in the notebooks.
- Make sure to select the correct column names for the dataset during data exploration to avoid errors.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### BibTeX Citation for GitHub Repository

```bibtex
@misc{heymans2024weather,
  author = {Heymans, Adrien},
  title = {Weather Prediction Project},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/adrien-heymans/weather-prediction-project}},
}

