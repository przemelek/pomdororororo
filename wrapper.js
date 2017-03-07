
chrome.storage.local.get(function(items) {
  var url = items["url"];
  if (!url) url="https://trello.com";
  console.log(url);
  webview.src=url;
  console.log("toster");
  console.log(webview.src);
});
webview.addEventListener('loadcommit', function(event) {
  var url = event.url;
  chrome.storage.local.set({url:url});
});
