import fixedNavbar from "./nav-bar.js";
// import loading from "./loading.js";
import loadImage from "./product-view.js";
import favicon from "./favicon.js";
import changeWishlistIcon from "./changeWishlistIcon.js";
import hoverAnimation from "./animations.js";
import footerYear from "./footer-year.js";
import smoothScroll from "./smooth-scroll.js";
import newsletterSubmitEvent from "./newsletter.js";

// Loading function
// loading();

// Navbar eventlistener
window.addEventListener("load", fixedNavbar);

// Year
footerYear();

// Function for loading the images on the products page
loadImage();

// Newsletter subscription event
newsletterSubmitEvent();

// Favicon
favicon();

// Change the wishlist icon. changes color when clicked
window.addEventListener("load", changeWishlistIcon);

// Adds "Click here on hover"
window.addEventListener("load", hoverAnimation);

// Smooth Scroll using the up and down keys
smoothScroll();
