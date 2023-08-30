let error1= document.getElementById("required1");
let error2= document.getElementById("required2");
let error3= document.getElementById("required3");
let error4= document.getElementById("required4");
let error5= document.getElementById("required5");
let error6= document.getElementById("required6");
let fname = document.getElementById("fname");
let lname = document.getElementById("lname");
let username = document.getElementById("username");
let mail = document.getElementById("mail");
let password = document.getElementById("password");
let cpassword = document.getElementById("cpassword");
let form = document.getElementById("form");
let submit = document.getElementById("btn");

var validRegex = /^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/;

form.addEventListener("submit", required)
function required(e){
  e.preventDefault()

  if (fname.value ===''){
    error1.style.display = "block";
    return;
  }
  error1.style.display = "none"

  if (lname.value ===''){
    error2.style.display = "block";
    return;
  }
  error2.style.display = "none"
  
  if (username.value ===''){
    error3.style.display = "block";
    return;
  }
  error3.style.display = "none"

  if (!mail.value.match(validRegex) || mail.value ==='') {
    mail.style.color = "red";
    mail.style.border = "1px solid red";
    error4.style.display= "block";
    return;
  }
  error4.style.display = "none";
  mail.style.border = "1px solid #767A77";
  mail.style.color = "#767A77"

  if(password.value === ''){
    error5.style.display = "block"
    return;
  }
  error5.style.display = "none"
  

  if(cpassword.value !== password.value){
    error6.style.display = "block"
    return;
  }
  
  error6.style.display = "none"

  if (fname.value !=="" && lname.value !=="" && username.value !=="" &&
    password.value !=="" && (mail.value.match(validRegex) && mail.value !=='')
    && cpassword.value === password.value ){
    submit.style.backgroundColor = "#1D4025"
    submit.style.color = "#ffffff"

    
    const csrfmiddlewaretoken = form.csrfmiddlewaretoken.value
    var data = {
      username: username,
      firstname:fname,
      lastname:lname,
      password:password,
      email:mail
    }
    fetch("/signup",{
      method:"POST",
      headers: { "X-CSRFToken": csrfmiddlewaretoken, "Content-Type": "application/json" },
      body: data
      // credentials: 'same-origin',
    })
    return true
  }
}