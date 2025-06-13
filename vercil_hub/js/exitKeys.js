document.addEventListener('keydown', function(event) {
  if (event.key === "Escape" || event.key === "Backspace") {
    if (typeof exitRedirectURL !== "undefined") {
      window.location.href = exitRedirectURL;
    } else {
      console.warn("exitRedirectURL is not defined.");
    }
  }
});