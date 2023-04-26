function footerYear() {
  const year = new Date().getFullYear();
  const footerYear = document.getElementById("footer-year");
  footerYear.innerHTML = `© Luku Store.nl  ${year}`;
}

export default footerYear;
