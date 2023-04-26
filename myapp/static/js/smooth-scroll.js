document.addEventListener("keydown", function (event) {
  if (event.keyCode === 38) {
    // Up arrow key is pressed
    smoothScroll(-400); // Scroll up by 50 pixels
  } else if (event.keyCode === 40) {
    // Down arrow key is pressed
    smoothScroll(400); // Scroll down by 50 pixels
  }
});

function smoothScroll(amount) {
  var start = window.pageYOffset;
  var target = start + amount;
  var duration = 500; // Duration in milliseconds

  function animate(currentTime) {
    var elapsedTime = currentTime - startTime;
    var position = easeInOut(elapsedTime, start, amount, duration);
    window.scrollTo(0, position);
    if (elapsedTime < duration) {
      requestAnimationFrame(animate);
    }
  }

  function easeInOut(t, b, c, d) {
    t /= d / 2;
    if (t < 1) return (c / 2) * t * t + b;
    t--;
    return (-c / 2) * (t * (t - 2) - 1) + b;
  }

  var startTime = performance.now();
  requestAnimationFrame(animate);
}

export default smoothScroll;
