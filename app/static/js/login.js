const $submit = document.getElementById("submit"),
      $password = document.getElementById("password"),
      $username = document.getElementById("username"),
      $visible = document.getElementById("visible");

document.addEventListener("change", (e) => {
    if (e.target === $visible) {
        $password.type = $visible.checked ? "text" : "password";
    }
});

document.addEventListener("click", (e) => {
    if (e.target === $submit) {
        e.preventDefault();
        if (validateInput($username.value, $password.value)) {
            loginUser($username.value, $password.value);
        }
    }
});

function validateInput(username, password) {
    if (username.length > 5 && password.length > 8) {
        return true;
    } else {
        alert("El nombre de usuario debe tener más de 5 caracteres y la contraseña más de 8 caracteres.");
        return false;
    }
}

function loginUser(username, password) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("{% url 'login' %}", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "{% url 'home' %}";
        } else {
            alert("Error al iniciar sesión. Por favor, verifica tus credenciales.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
