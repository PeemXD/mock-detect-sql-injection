const form = document.getElementById("login-form");
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = {
    username: form.elements.username.value,
    password: form.elements.password.value,
  };

  // Send a request to the server to check if the email and password exist
  try {
    async function login1() {
      const response = await fetch("http://localhost:3000/login", {
        method: "POST",
        mode: "cors",
        body: JSON.stringify({ data }),
        headers: { "Content-Type": "application/json" },
      });
      console.log(response);
      let data2 = await response.json();
      return data2;
    }

    login1().then((data2) => {
      if (data2.success) {
        window.location.replace("show.html");
      } else {
        alert("Invalid email or password");
      }
    });
  } catch (error) {
    alert(error);
  }
});
