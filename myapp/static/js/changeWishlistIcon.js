function changeWishlistIcon() {
  const wishlistIcons = document.querySelectorAll("i.wishlist");
  const ratingStar = document.querySelectorAll("i.rating-star-detail");

  wishlistIcons.forEach((icon) => {
    icon.addEventListener("click", () => {
      if (icon.classList.contains("fa-regular")) {
        icon.classList.remove("fa-regular");
        icon.classList.add("fa-solid");
      } else {
        icon.classList.remove("fa-solid");
        icon.classList.add("fa-regular");
      }
      console.log("Wishlist icon changed successfully.");
    });
  });

  ratingStar.forEach((star) => {
    star.addEventListener("click", () => {
      if (star.classList.contains("fa-regular")) {
        star.classList.remove("fa-regular");
        star.classList.add("fa-solid");
        star.style.color = "#b08f27";
      } else {
        star.classList.remove("fa-solid");
        star.classList.add("fa-regular");
        star.style.color = "";
      }
      console.log("Wishlist icon changed successfully.");
    });
  });
}
export default changeWishlistIcon;
