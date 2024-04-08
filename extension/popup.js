document.getElementById('runScriptsBtn').addEventListener('click', () => {
    chrome.runtime.sendMessage({action: 'executeScripts'});
  });
  