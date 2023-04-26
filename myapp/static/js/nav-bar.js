function fixedNavbar() {
  const nav = document.querySelector(".navigation-bar");

  const onScroll = (event) => {
    const scrollPosition = event.target.scrollingElement.scrollTop;

    if (scrollPosition > 400) {
      if (!nav.classList.contains("scrolled-down")) {
        nav.classList.add("scrolled-down");
        nav.style.position = "fixed";
      }
    } else {
      if (nav.classList.contains("scrolled-down")) {
        nav.classList.remove("scrolled-down");
        nav.style.position = "";
      }
    }
  };

  document.addEventListener("scroll", onScroll);
}

export default fixedNavbar;
