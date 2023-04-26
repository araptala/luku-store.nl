// Favicon

function favicon() {
  var link = document.createElement("link");
  link.rel = "shortcut icon";
  link.type = "image/x-icon";
  link.href = "/static/favicon.ico";
  document.getElementsByTagName("head")[0].appendChild(link);
}

export default favicon;
