document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM cargado, buscando el botón toggleEdicion');
    
    var toggleButton = document.getElementById('toggleEdicion');
    
    if (toggleButton) {
        
        toggleButton.addEventListener('click', function() {
            console.log('Botón toggleEdicion clickeado');
            
            var detalles = document.getElementById('contratodetails');
            var formulario = document.getElementById('formularioEdicion');
            
            if (formulario.classList.contains('hidden')) {
                detalles.classList.add('hidden');
                formulario.classList.remove('hidden');
                this.textContent = 'Cancelar Edición';
                this.classList.remove('bg-blue-500', 'text-white');
                this.classList.add('bg-red-500', 'text-red-100');
            } else {
                detalles.classList.remove('hidden');
                formulario.classList.add('hidden');
                this.textContent = 'Editar Contrato';
                this.classList.remove('bg-red-500', 'text-red-100');
                this.classList.add('bg-blue-500', 'text-white');
            }
        });
    } else {
        console.log('Botón toggleEdicion no encontrado');
    }
});
