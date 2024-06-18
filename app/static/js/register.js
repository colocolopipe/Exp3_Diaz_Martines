const $submit = document.getElementById("submit"),
      $password = document.getElementById("password"),
      $confirmPassword = document.getElementById("confirm-password"),
      $username = document.getElementById("username"),
      $email = document.getElementById("email"),
      $visible = document.getElementById("visible"),
      $back = document.getElementById("back");

document.addEventListener("change", (e) => {
    if (e.target === $visible) {
        const type = $visible.checked ? "text" : "password";
        $password.type = type;
        $confirmPassword.type = type;
    }
});

document.addEventListener("submit", (e) => {
    e.preventDefault();
    let isValid = true;

    if ($username.value === "") {
        showTooltip($username, "El nombre de usuario es obligatorio.");
        isValid = false;
    }

    if ($email.value === "") {
        showTooltip($email, "El correo electrónico es obligatorio.");
        isValid = false;
    }

    if ($password.value === "") {
        showTooltip($password, "La contraseña es obligatoria.");
        isValid = false;
    }

    if ($confirmPassword.value === "") {
        showTooltip($confirmPassword, "Confirmar la contraseña es obligatorio.");
        isValid = false;
    }

    if ($password.value !== $confirmPassword.value) {
        showTooltip($confirmPassword, "Las contraseñas no coinciden.");
        isValid = false;
    }

    if (isValid) {
        // Aquí puedes añadir la lógica para crear la cuenta (por ejemplo, enviar los datos a un servidor)
        alert("Cuenta creada con éxito!");
        window.location.href = "index.html";
    }
});

document.addEventListener("click", (e) => {
    if (e.target === $back) {
        window.location.href = "index.html";
    }
});

function showTooltip(element, message) {
    element.setCustomValidity(message);
    element.reportValidity();
    element.addEventListener("input", function clearCustomValidity() {
        element.setCustomValidity("");
        element.removeEventListener("input", clearCustomValidity);
    });
}
