let error1 = document.getElementById("required1");
let error2 = document.getElementById("required2");
let mail = document.getElementById("mail");
let password = document.getElementById("password");
let form = document.getElementById("form");
let submit = document.getElementById("btn");

var validRegex = /^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/;

form.addEventListener("submit", function (e) {
  e.preventDefault();

  // Validation checks

  if (!mail.value.match(validRegex) || mail.value === '') {
    mail.style.color = "red";
    mail.style.border = "1px solid red";
    error2.style.display = "block";
  }
  else{
    return true;
  }

  if (password.value === '') {
    error1.style.display = "block";
  }
  else{
    return true;
  }

  // If all validation checks pass, submit the form
  if (
    password.value !== "" &&
    (mail.value.match(validRegex) && mail.value !== "")
  ) {
    // You can choose to submit the form here or return true
    // Use the correct endpoint for user registration in your fetch request
    const csrfmiddlewaretoken = form.csrfmiddlewaretoken.value;
    const formData = new FormData(form);

    fetch("/login", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfmiddlewaretoken,
      },
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the server (e.g., display success message)
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
});
