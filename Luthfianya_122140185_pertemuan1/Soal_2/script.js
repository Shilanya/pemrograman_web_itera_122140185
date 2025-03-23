function sapaNama(nama) {
    return `Halo, ${nama}! Selamat belajar JavaScript!`;
}

document.getElementById("sapa-button").addEventListener("click", function() {
    const nama = document.getElementById("nama-input").value;
    if (nama.trim() === "") {
        document.getElementById("sapa-output").innerHTML = 
            `<p style="color: red;">Silakan masukkan nama Anda terlebih dahulu!</p>`;
    } else {
        const pesan = sapaNama(nama);
        document.getElementById("sapa-output").innerHTML = 
            `<p style="color: green;">${pesan}</p>`;
    }
});

function hitung(operator) {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    let hasil;

    if (isNaN(angka1)) {
        document.getElementById("hasil-kalkulator").innerHTML = "Masukkan angka pertama!";
        return;
    }

    if (operator !== 'sqrt' && isNaN(angka2)) {
        document.getElementById("hasil-kalkulator").innerHTML = "Masukkan angka kedua!";
        return;
    }

    switch (operator) {
        case '+':
            hasil = angka1 + angka2;
            break;
        case '-':
            hasil = angka1 - angka2;
            break;
        case '*':
            hasil = angka1 * angka2;
            break;
        case '/':
            hasil = angka2 !== 0 ? angka1 / angka2 : "Error: Pembagian dengan nol tidak diperbolehkan";
            break;
        case '^':
            hasil = Math.pow(angka1, angka2);
            break;
        case 'sqrt':
            hasil = angka1 >= 0 ? Math.sqrt(angka1) : "Error: Tidak dapat menghitung akar negatif";
            break;
        case '%':
            hasil = angka1 % angka2;
            break;
        default:
            hasil = "Operasi tidak valid";
    }

    document.getElementById("hasil-kalkulator").innerHTML = `Hasil: ${hasil}`;
}
