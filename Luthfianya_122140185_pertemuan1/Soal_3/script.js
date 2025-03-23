document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Mencegah reload halaman

    // Ambil nilai input
    let nama = document.getElementById("nama").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    // Reset pesan error
    document.getElementById("error-nama").innerText = "";
    document.getElementById("error-email").innerText = "";
    document.getElementById("error-password").innerText = "";

    let isValid = true;

    // Validasi nama (minimal 4 karakter)
    if (nama.length < 4) {
        document.getElementById("error-nama").innerText = "Nama harus lebih dari 3 karakter!";
        isValid = false;
    }

    // Validasi email dengan regex
    let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email)) {
        document.getElementById("error-email").innerText = "Email tidak valid!";
        isValid = false;
    }

    // Validasi password (minimal 8 karakter)
    if (password.length < 8) {
        document.getElementById("error-password").innerText = "Password harus minimal 8 karakter!";
        isValid = false;
    }

    // Jika valid, tampilkan alert
    if (isValid) {
        alert("Form berhasil dikirim!");
    }
});
