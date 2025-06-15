const createWindow = () => {
// Create the browser window.
const mainWindow = new BrowserWindow({
    width: 1000,
    height: 800,
    webPreferences: {
        nodeIntegration: true,
        contextIsolation: false,
        enableRemoteModule: true,
    }
});
// and load the index.html of the app.
mainWindow.loadFile(path.join(_dirname, 'index.html'));

// Open the DevTools.
// mainwindow.webContents.openDevTools();
};