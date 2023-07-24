let error1= document.getElementById("error1");
let error2= document.getElementById("error2");
let username = document.getElementById("username");
let password = document.getElementById("password");
let submit = document.getElementById("btn");

let form = document.getElementById("form");
form.addEventListener("submit", required)
function required(e){
  e.preveventDefault()

  if (username.value ===""){
    error1.style.display = "block"
    return false
  }
  error1.style.display = "none"

  if (password.value ===""){
    error2.style.display = "block"
    return false
  }
  error2.style.display = "none"

  if (username.value !=="" && password.value !==""){
    submit.style.backgroundColor = "#1D4025"
    submit.style.color = "#ffffff"

    const csrfmiddlewaretoken = form.csrfmiddlewaretoken.value
    var data = new FormData();
    data.append("json", JSON.stringify( obj ) );
    let data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);
    fetch("/login",{
      method:"POST",
      headers: { "X-CSRFToken": csrfmiddlewaretoken, "Content-Type": "application/json" },
      body: data,
      // credentials: 'same-origin',
    })
    return true
  }

}