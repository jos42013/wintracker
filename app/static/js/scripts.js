// This file is intentionally left blank.

// Contenu du header
const headerHTML = `
<header class="header">
    <p class="logo">
        <samp>WinTracker</samp>
    </p>
    <nav>
        <ul>
            <li><a href="#">Home</a></li>
        </ul>
    </nav>
    <div class="search-container">
        <input type="text" class="search-box" id="searchInput" placeholder="Rechercher...">
        <button class="search-button" onclick="searchFunction()">Rechercher</button>
    </div>
</header>
`;

// Contenu du footer
const footerHTML = `
<footer>
    <p class="logo">
        &copy; 2025
        <samp>WinTracker</samp>
    </p>
    
</footer>
`;

// Insérer le header et le footer dans la page
document.addEventListener("DOMContentLoaded", () => {
    document.body.insertAdjacentHTML("afterbegin", headerHTML);
    document.body.insertAdjacentHTML("beforeend", footerHTML);
});

document.addEventListener('DOMContentLoaded', () => {
    // Load initial data
    fetchCurrentWindows();
    fetchLogs();
    loadConfigForm();
    
    // Set up periodic refreshes
    setInterval(fetchCurrentWindows, 5000);
    setInterval(fetchLogs, 10000);
});

function fetchCurrentWindows() {
    fetch('/api/windows')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('current-windows-list');
            container.innerHTML = '<ul>' + 
                data.windows.filter(w => w).map(w => `<li>${w}</li>`).join('') + 
                '</ul>';
        });
}

function fetchLogs() {
    fetch('/api/logs')
        .then(response => response.json())
        .then(logs => {
            const container = document.getElementById('logs-container');
            container.innerHTML = logs.slice().reverse().map(log => `
                <div class="log-entry">
                    <strong>${new Date(log.timestamp).toLocaleString()}</strong>
                    <div>${log.windows.filter(w => w).join(', ')}</div>
                </div>
            `).join('');
        });
}
function fetchWindowStatistics() {
    fetch('/api/statistics')
        .then(response => response.json())
        .then(stats => {
            const container = document.getElementById('window-stats-container');
            container.innerHTML = '<ul>' +
                Object.entries(stats).map(([window, count]) => `<li>${window}: ${count} times</li>`).join('') +
                '</ul>';
        });
}

// Ajouter un appel périodique pour mettre à jour les statistiques
document.addEventListener('DOMContentLoaded', () => {
    fetchWindowStatistics();
    setInterval(fetchWindowStatistics, 15000); // Mettre à jour toutes les 15 secondes
});
function fetchWindowStatisticsGraph() {
    const img = document.getElementById('window-stats-graph');
    img.src = '/api/window_statistics';
}

// Ajouter un appel pour charger le graphique au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    fetchWindowStatisticsGraph();
});

function loadConfigForm() {
    fetch('/api/config')
        .then(response => response.json())
        .then(config => {
            const form = document.getElementById('config-form');
            console.log(form);
            
            form.innerHTML = `
                <div class="form-group">
                    <label for="log-interval">Log Interval (seconds):</label>
                    <input type="number" id="log-interval" value="${config.log_interval}">
                </div>
                <div class="form-group">
                    <label for="remote-url">Remote Server URL:</label>
                    <input type="text" id="remote-url" value="${config.remote_server_url}">
                </div>
                <div class="form-group">
                    <label>
                        <input type="checkbox" id="remote-logging" ${config.remote_logging ? 'checked' : ''}>
                        Enable Remote Logging
                    </label>
                </div>
                <button type="button" onclick="saveConfig()">Save Configuration</button>
            `;
        });
}

function saveConfig() {
    const newConfig = {
        log_interval: parseInt(document.getElementById('log-interval').value),
        remote_server_url: document.getElementById('remote-url').value,
        remote_logging: document.getElementById('remote-logging').checked
    };
    
    fetch('/api/config', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newConfig)
    }).then(() => {
        alert('Configuration saved successfully');
    });
}