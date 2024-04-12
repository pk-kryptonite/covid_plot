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


