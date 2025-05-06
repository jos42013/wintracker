# Définit les endpoints (/api/windows, /dashboard)
from flask import Flask, render_template, jsonify, send_file, request
from logger import LogManager
from monitor import WindowMonitor
from config import Config
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
config = Config()
log_manager = LogManager(config)
monitor = WindowMonitor(log_manager)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/windows', methods=['GET'])
def get_windows():
    windows = monitor.get_open_windows()
    return jsonify({
        'windows': windows,
        'timestamp': monitor.get_current_timestamp()
    })

@app.route('/api/logs', methods=['GET'])
def get_logs():
    return jsonify(log_manager.get_logs())

@app.route('/api/config', methods=['GET', 'POST'])
def handle_config():
    if request.method == 'POST':
        new_config = request.json
        config.update_config(new_config)
        return jsonify({'status': 'success'})
    return jsonify(config.get_config())

@app.route('/api/window_statistics', methods=['GET'])
def get_window_statistics():
    logs = log_manager.get_logs()
    stats = {}

    # Calculer les statistiques
    for log in logs:
        for window in log['windows']:
            if window in stats:
                stats[window] += 1
            else:
                stats[window] = 1

    # Créer un DataFrame pandas
    import pandas as pd
    df = pd.DataFrame(list(stats.items()), columns=['Window', 'Count'])

    # Générer un graphique
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Count', y='Window', data=df.sort_values('Count', ascending=False), palette="viridis")
    plt.title("Fenêtres les plus utilisées")
    plt.xlabel("Nombre d'occurrences")
    plt.ylabel("Fenêtres")

    # Sauvegarder le graphique dans un buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Retourner le graphique sous forme d'image
    return send_file(buffer, mimetype='image/png')