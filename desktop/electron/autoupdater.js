// 🔄 DramaFlow AI - Auto Update System (Electron Updater Layer)
// Enables silent updates + version check + restart flow

const { autoUpdater } = require('electron-updater');
const { dialog } = require('electron');

function initAutoUpdater(mainWindow) {

    autoUpdater.autoDownload = true;
    autoUpdater.autoInstallOnAppQuit = true;

    autoUpdater.on('update-available', () => {
        mainWindow.webContents.send('update-status', 'Update available... downloading');
    });

    autoUpdater.on('update-downloaded', () => {
        dialog.showMessageBox(mainWindow, {
            type: 'info',
            title: 'Update Ready',
            message: 'A new version has been downloaded. Restart to apply update.'
        });

        autoUpdater.quitAndInstall();
    });

    autoUpdater.on('error', (err) => {
        console.error('AutoUpdater error:', err);
    });

    autoUpdater.checkForUpdatesAndNotify();
}

module.exports = { initAutoUpdater };