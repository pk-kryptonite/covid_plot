# COVID-19 Analysis Web Application

This is a web application built with Flask that allows users to analyze COVID-19 data provided in a JSON format. The application provides visualizations of the data in the form of line plots, scatter plots, and statistics summaries.

## Features

- Upload JSON file: Users can upload a JSON file containing COVID-19 data.
- Data Analysis: The application analyzes the uploaded data and generates visualizations.
- Visualizations:
  - Time Series Line Plot: Shows the trend of COVID-19 cases over time.
  - Scatter Plot: Displays the distribution of COVID-19 cases.
  - Statistics Summary: Presents the lowest, average, and highest values of COVID-19 cases.
- Downloadable Images: Users can download the generated visualizations through hovering on each image then click.

## Installation

### Local Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/pk-kryptonite/covid_plot.git
    ```

2. Navigate to the project directory:

    ```
    cd covid_plot
    ```
4. create virtual environment:

    ```
    python -m venv venv && source venv/bin/activate 
    ```
3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5000`.
6. Upload a JSON file containing COVID-19 data using the provided form.
7. Once the data is uploaded, the application will display visualizations of the data.
8. Hover over each graph to see the download option for the respective image.

### Docker Installation

1. Install Docker on your machine if you haven't already. You can download Docker Desktop from the [official website](https://www.docker.com/products/docker-desktop).

2. Run docker image

    ```
    docker run -p 5000:5000 phelok/covid_plot:1.0.0
    ```

3. Docker inspect to find the IPAddress

    ```
    docker inspect <container-id>
    ```

4. Open your web browser and go to `<container IPAddress>:5000`.
5. Follow the same steps as described in the "Local Installation" section of the README to use the web application.

This method allows you to run the application within a Docker container without needing to install the dependencies directly on your local machine. Docker will handle the environment setup and dependencies for you, ensuring consistency across different environments.

### Detailed explaination on how the web application work

#### Upload JSON File: 

The application allows users to upload a JSON file containing COVID-19 data.

#### Data Analysis: 
After the user uploads a JSON file, this application extracts the relevant information, and then cleans the data (this includes INT written as string and verifying the dates) eg "Active Cases": "25 565" is supposed to be "Active Cases": 25565.

#### Visualization:

Once the data is analyzed, the application generates visualizations such as:

Time Series Line Plot: This plot shows the trend of COVID-19 cases over time. It typically includes lines representing total confirmed cases, total deaths, total recovered cases, and active cases.

Scatter Plot: This plot displays the distribution of COVID-19 cases. It allows users to see how different types of cases (confirmed, deaths, recovered, active) are distributed over time.

Statistics Summary: This summary presents the lowest, average, and highest values of COVID-19 cases. It provides a quick overview of the data statistics.
#### Downloadable Images: 
Each visualization generated by the application is downloadable. Users can hover over each graph to see a download option for the respective image. This allows users to save the visualizations for further analysis or sharing.

#### User Interface: 

The web application provides a simple user interface for interacting with the data and visualizations. Users can upload a JSON file, view the visualizations, and download the images directly from their web browser.

#### Technologies Used: 

The application is built using Python and Flask for the backend server, HTML/CSS for the frontend user interface, and Bootstrap for styling. It has been deployed on a public repository in docker.


