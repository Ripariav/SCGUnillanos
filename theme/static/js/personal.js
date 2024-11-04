document.addEventListener('DOMContentLoaded', function () {
    // Obtén los elementos de los radio buttons
    const radioSupervisores = document.querySelector('input[value="supervisores"]');
    const radioProveedores = document.querySelector('input[value="proveedores"]');

    // Obtén las secciones
    const sectionSupervisores = document.getElementById('section-supervisores');
    const sectionProveedores = document.getElementById('section-proveedores');

    // Función para mostrar/ocultar secciones
    function toggleSections() {
        if (radioSupervisores.checked) {
            sectionSupervisores.classList.remove('hidden');
            sectionProveedores.classList.add('hidden');
        } else if (radioProveedores.checked) {
            sectionProveedores.classList.remove('hidden');
            sectionSupervisores.classList.add('hidden');
        }
    }

    // Llama a la función cuando el DOM esté cargado para establecer el estado inicial
    toggleSections();

    // Agrega los event listeners para cambiar de sección cuando se selecciona un radio button
    radioSupervisores.addEventListener('change', toggleSections);
    radioProveedores.addEventListener('change', toggleSections);
});