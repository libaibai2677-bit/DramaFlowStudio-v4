// 🖥️ DramaFlow AI - Electron Desktop Wrapper (Production Shell)
// Goal: wrap web UI into native desktop app window

const { app, BrowserWindow } = require('electron');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        backgroundColor: '#0a0f1c',
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    // 🌐 Load local web UI (from docker/nginx or local server)
    mainWindow.loadURL('http://localhost:3000');

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
