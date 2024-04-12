from flask import Flask, render_template, request
import json
import os
import datetime
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


def clean_data(data):
    dates = []
    confirmed_cases = []
    deaths = []
    recovered = []
    active_cases = []

    for entry in data:
        try:
            date = datetime.datetime.strptime(entry['Date'], "%Y/%m/%d").date()
        except ValueError:
            continue

        dates.append(date)
        confirmed_cases_val = entry.get('Total Confirmed Cases')
        deaths_val = entry.get('Total Deaths')
        recovered_val = entry.get('Total Recovered')
        active_cases_val = entry.get('Active Cases')

        confirmed_cases.append(clean_value_to_int(confirmed_cases_val))
        deaths.append(clean_value_to_int(deaths_val))
        recovered.append(clean_value_to_int(recovered_val))
        active_cases.append(clean_value_to_int(active_cases_val))

    return dates, confirmed_cases, deaths, recovered, active_cases


def clean_value_to_int(value):
    if isinstance(value, str):
        return int(value.replace(' ', ''))
    elif isinstance(value, int):
        return value
    else:
        return None


def create_line_plot(dates, confirmed_cases, deaths, recovered, active_cases):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, confirmed_cases, label='Total Confirmed Cases')
    plt.plot(dates, deaths, label='Total Deaths')
    plt.plot(dates, recovered, label='Total Recovered')
    plt.plot(dates, active_cases, label='Active Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title('COVID-19 Cases Over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path = 'static/line_plot.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path

def create_scatter_plot(dates, confirmed_cases, deaths, recovered, active_cases):
    plt.figure(figsize=(10, 6))
    plt.scatter(dates, confirmed_cases, color='red', marker='o', label='Confirmed Cases')
    plt.scatter(dates, deaths, color='blue', marker='o', label='Deaths')
    plt.scatter(dates, recovered, color='green', marker='o', label='Recovered')
    plt.scatter(dates, active_cases, color='orange', marker='o', label='Active Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title('COVID-19 Cases Scatter Plot')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path = 'static/scatter_plot.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path


def plot_stats(confirmed_cases, deaths, recovered, active_cases):
    stats = {
        'Confirmed Cases': [np.min(confirmed_cases), np.mean(confirmed_cases), np.max(confirmed_cases)],
        'Deaths': [np.min(deaths), np.mean(deaths), np.max(deaths)],
        'Recovered': [np.min(recovered), np.mean(recovered), np.max(recovered)],
        'Active Cases': [np.min(active_cases), np.mean(active_cases), np.max(active_cases)]
    }
    categories = list(stats.keys())
    values = np.array(list(stats.values()))
    plt.figure(figsize=(10, 6))
    bar_width = 0.2
    index = np.arange(len(categories))
    plt.bar(index - bar_width, values[:, 0], bar_width, label='Lowest')
    plt.bar(index, values[:, 1], bar_width, label='Average')
    plt.bar(index + bar_width, values[:, 2], bar_width, label='Highest')
    plt.xlabel('Category')
    plt.ylabel('Number of Cases')
    plt.title('COVID-19 Cases Statistics')
    plt.xticks(index, categories)
    plt.legend()
    plt.tight_layout()
    plot_path = 'static/stats_plot.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.json'):
            filename = 'uploads/' + file.filename
            file.save(filename)
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                if all(key in data[0] for key in ['Date', 'Total Confirmed Cases', 'Total Deaths', 'Total Recovered', 'Active Cases']):
                    dates, confirmed_cases, deaths, recovered, active_cases = clean_data(data)
                    line_plot_path = create_line_plot(dates, confirmed_cases, deaths, recovered, active_cases)
                    scatter_plot_path = create_scatter_plot(dates, confirmed_cases, deaths, recovered, active_cases)
                    stats_plot_path = plot_stats(confirmed_cases, deaths, recovered, active_cases)
                    return render_template('index.html', line_plot=line_plot_path, scatter_plot=scatter_plot_path, stats_plot=stats_plot_path)
                else:
                    os.remove(filename)
                    return render_template('index.html', error_message='Error: Invalid JSON format')
        else:
            return render_template('index.html', error_message='Error: Please upload a JSON file')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
