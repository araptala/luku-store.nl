function newsletterSubmitEvent() {
  const form = document.querySelector("#newsletter-form");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const email = document.querySelector("#newsletter-email").value;
    const termsCheckbox = document.querySelector("#terms-checkbox");
    if (!termsCheckbox.checked) {
      alert("Please agree to the terms and privacy policy before subscribing.");
      return;
    }
    // You can add your own validation code here before submitting the form
    alert(`Thank you for subscribing to our newsletter, ${email}!`);
    form.reset(); // Reset the form after submission
  });
}
export default newsletterSubmitEvent;
