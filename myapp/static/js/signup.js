const container = document.querySelector("container");
const loginNow = document.querySelector("login-now");
const image1 = document.getElementById("login-image");
const image2 = document.getElementById("signin-image");
const form = document.querySelector("form");

// Dnamically displaying text on the webpage

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Get the title, subtitle, and sign-in elements
  const title = document.querySelector(".create-title");
  const subTitle = document.querySelector(".sub-title");
  const btn = document.querySelector(".btn");
  const login = document.querySelector(".login");
  const signinNow = document.querySelector("signin-now");

  // Dynamically display on the HTML with the elements
  title.innerHTML = "Create an Account";
  subTitle.innerHTML = "Hello there, Let's start your journey with us.";
  btn.innerHTML = "SignUpp";
  login.innerHTML = "Already have an Account? ";
  signinNow.innerHTML = "Login Now";
  console.log("didnt work");
});

// function changeImage() {
//   if (image1.classList.contains("fade-out")) {
//     title.textContent = "Nice to see you again!";
//     subTitle.textContent = "Jump in!";
//     login.textContent = "Don't have an account?";
//     btn.textContent = `Sign In`;
//   }
//   image1.classList.add("fade-out");
//   image2.classList.add("fade-in");
// }

// loginNow.addEventListener("click", () => changeImage());

// // FORM
// form.addEventListener("submit", (event) => {
//   // Prevent the default form submission behavior
//   event.preventDefault();

//   // Get the values of the email/username and password fields
//   const email = document.querySelector("#email").value;
//   const password = document.querySelector("#password").value;

//   const formData = {
//     email: email,
//     password: password,
//   };

//   // Send the form data to the Django backend
//   fetch("/views/signup/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(formData),
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Network response was not ok");
//       }
//       return response.json();
//     })
//     .then((data) => {
//       // Handle the response data as needed
//       console.log(data);
//     })
//     .catch((error) => {
//       // Handle errors as needed
//       console.error("Error:", error);
//     });

//   // Get the value of the checkbox for accepting terms
//   // const termsAccepted = document.querySelector("#terms").checked;

//   // Check if the user has accepted the terms
//   // if (!termsAccepted) {
//   //   alert("Please accept the terms to proceed.");
//   //   return;
//   // }

//   // Submit the form data to the server
// });
