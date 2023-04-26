function hoverAnimation() {
  const hoverAnimation = document.querySelectorAll(".hover-animate");

  hoverAnimation.forEach((link) => {
    link.addEventListener("click", () => {
      // If the following statement is TRUE:
      if (link.classList.contains("hover-animate")) {
        // Therefore, do something
        // In this case, remove that class:
        link.textContent = "Click here >";
      } else {
        // IF first "if" is FALSE:

        // Remove whatever is present there
        link.classList.remove("");

        // Then add this
        link.classList.add("hover-animate");
      }
    });
  });
}
export default hoverAnimation;
