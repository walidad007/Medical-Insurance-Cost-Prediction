import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('medical_insurance_cost_prediction.pkl')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.Div([
        html.H1("Medical Insurance Cost Prediction",
        style={
        'text-align': 'center',
        'color': 'red',
        # 'font-size': '3em',  # Increase the font size
        'font-weight': 'bold',  # Make the font bold
        # 'text-shadow': '2px 2px 4px #000000',  # Add a text shadow for a 3D effect
        'padding': '20px',  # Add some padding around the text
        'background-color': 'white',  # Add a background color to make the text stand out
        'border-radius': '10px',  # Round the corners of the background
        'box-shadow': '0px 0px 1px #000000'  # Add a shadow around the element 
        }),

        html.Div([
            dcc.Input(id='age', type='number', placeholder='Age', 
                      style={'margin': '10px', 'padding': '10px'}),

            dcc.Dropdown(id='sex', options=[
                {'label': 'Male', 'value': 'male'},
                {'label': 'Female', 'value': 'female'}
            ], placeholder='Sex', style={'margin': '10px', 'padding': '10px'}),

            dcc.Input(id='bmi', type='number', placeholder='BMI', 
                      style={'margin': '10px', 'padding': '10px'}),

            dcc.Input(id='children', type='number', placeholder='Children', 
                      style={'margin': '10px', 'padding': '10px'}),

            dcc.Dropdown(id='smoker', options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ], placeholder='Smoker', style={'margin': '10px', 'padding': '10px'}),

            dcc.Dropdown(id='region', options=[
                {'label': 'Northwest', 'value': 'northwest'},
                {'label': 'Southeast', 'value': 'southeast'},
                {'label': 'Southwest', 'value': 'southwest'},
                {'label': 'Northeast', 'value': 'northeast'}
            ], placeholder='Region', style={'margin': '10px', 'padding': '10px'}),

            html.Button('Predict Price', id='predict_button', n_clicks=0,
                        style={'margin': '10px', 'padding': '10px', 'background-color': '#007BFF',
                               'color': 'white'}),
        ], style={'text-align': 'center'}),

        html.Div(id='prediction_output', style={'text-align': 'center', 'font-size': '20px', 'margin-top': '20px'})
    ], style={'width': '50%', 'margin': '0 auto', 'border': '2px solid #007BFF', 'padding': '20px', 'border-radius': '10px'})
])

# Define callback to update
@app.callback(
    Output('prediction_output', 'children'),
    [Input('predict_button', 'n_clicks')],
    [State('age', 'value'),
     State('sex', 'value'),
     State('bmi', 'value'),
     State('children', 'value'),
     State('smoker', 'value'),
     State('region', 'value')]
)
def update_output(n_clicks, age, sex, bmi, children, smoker, region):
    if n_clicks > 0 and all(v is not None for v in [age, sex, bmi, children, smoker, region]):
        # Create a dataframe with the input values
        input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                  columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        # Apply one-hot encoding
        input_data = pd.get_dummies(input_data, columns=['sex', 'smoker', 'region'], drop_first=True)

        # Ensure all required columns are present
        for col in ['sex_male', 'smoker_yes', 'region_northwest', 'region_southeast', 'region_southwest']:
            if col not in input_data.columns:
                input_data[col] = 0

        # Reorder columns to match the training data
        input_data = input_data[['age', 'bmi', 'children', 'sex_male', 'smoker_yes', 'region_northwest', 'region_southeast', 'region_southwest']]

        # Predict
        prediction = model.predict(input_data)[0]
        return f'Predicted Insurance Cost: {prediction:.2f}'
    elif n_clicks > 0:
        return 'Please enter all values to get a prediction'
    return ''

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
