// LOADING

function loading() {
  window.addEventListener("load", function () {
    const loadingText = document.querySelector(".loading-text");
    loadingText.style.display = "none";
  });

  const links = document.querySelectorAll("a");
  for (const link of links) {
    link.addEventListener("click", function () {
      const loadingText = document.querySelector(".loading-text");
      loadingText.style.display = "block";
    });
  }
}
// END OF LOADING

export default loading;

// // LOADING

// function loading() {
//   window.addEventListener("load", function () {
//     const loadingText = document.querySelector(".loading-text");
//     setTimeout(function () {
//       loadingText.style.display = "none";
//     }, 5000); // Wait for 5 seconds before hiding the loading text
//   });

//   const links = document.querySelectorAll("a");
//   for (const link of links) {
//     link.addEventListener("click", function () {
//       const loadingText = document.querySelector(".loading-text");
//       loadingText.style.display = "block";
//     });
//   }
// }
// // END OF LOADING

// export default loading;
