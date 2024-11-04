// static/js/backupreminder.js

document.addEventListener("DOMContentLoaded", function () {
    const today = new Date();
    const lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
    const currentDay = today.getDate();
    const lastAlertShown = localStorage.getItem("backupAlertShown");

    // Verifica si es el último día del mes y si ya no se ha mostrado la alerta hoy
    if (currentDay === lastDayOfMonth && lastAlertShown !== today.toDateString()) {
        alert("¡Recuerda hacer una copia de seguridad antes de que termine el mes!");

        // Guarda en el almacenamiento local que ya se mostró la alerta hoy
        localStorage.setItem("backupAlertShown", today.toDateString());
    }
});
