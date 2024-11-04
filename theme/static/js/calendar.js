document.addEventListener('DOMContentLoaded', function () {
    // Inicializa flatpickr
    flatpickr(".flatpickr", {
        dateFormat: "Y-m-d",
        enableTime: false,
        locale: "es"
    });

    // Verifica si FullCalendar está definido
    console.log(FullCalendar); // Esto debería mostrar el objeto en la consola

    const calendarEl = document.getElementById('calendar');
    const tableEl = document.querySelector('table'); // Selecciona la tabla de contratos
    const calendarChangerBtn = document.getElementById('calendarChanger');

    // Verifica si calendarEl se ha encontrado
    if (!calendarEl) {
        console.error("El elemento del calendario no se encontró.");
        return; // Salir si no se encuentra el elemento
    }

    // Crea la instancia del calendario
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth', // Muestra el calendario en la vista de mes
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        events: window.contractsData.map(contract => ({
            title: contract.numero_contrato + ': ' + contract.descripcion,
            start: contract.plazo_fin,
            url: contract.documentos_cargados // Si quieres que se redirija al documento cargado al hacer clic
        })),
        locale: 'es' // Establece el idioma en español
    });

    // Renderiza el calendario
    calendar.render();

    // Añade el evento click para alternar la visibilidad de la tabla y del calendario
    calendarChangerBtn.addEventListener('click', function () {
        // Alterna la visibilidad del calendario y la tabla de contratos
        if (tableEl.classList.contains('hidden')) {
            tableEl.classList.remove('hidden');
            calendarEl.classList.add('hidden');
        } else {
            tableEl.classList.add('hidden');
            calendarEl.classList.remove('hidden');
        }
    });
});