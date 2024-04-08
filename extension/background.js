// background.js

// Function to send a message to the content script to execute Python scripts
function sendMessageToContentScript() {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, { action: 'executeScripts' });
  });
}

// Trigger the execution of Python scripts when the extension is installed or on certain events
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed.');
  // Execute sniff.py when the extension is installed
  executeScript('C://Users//HP//Documents//FINAL YEAR PROJECT//programs//project prototype 1//module one//sniff.py');
});

// Function to execute Python scripts
function executeScript(scriptName) {
  console.log('Executing Python script:', scriptName);
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const activeTab = tabs[0];
    if (activeTab.url && activeTab.url.startsWith('http')) {
      chrome.scripting.executeScript({
        target: { tabId: activeTab.id },
        function: () => {
          // Use fetch API to communicate with a backend server to execute Python scripts.
          // For simplicity, let's assume the scripts are executed using a backend server.
          fetch('http://127.0.0.1:5000/', {
            method: 'POST',
            body: JSON.stringify({ scriptName }),
            headers: {
              'Content-Type': 'application/json'
            }
          });
        }
      });
    } else {
      console.log('Active tab is not a regular web page.');
    }
  });
}
