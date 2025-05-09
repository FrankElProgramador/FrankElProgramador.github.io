function showAnalysisOptions() {
    const analysisType = document.getElementById('analysis-type').value;
    const extraOptions = document.getElementById('extra-options');
    
    if (analysisType) {
        extraOptions.style.display = 'block'; // Mostrar opciones adicionales
    } else {
        extraOptions.style.display = 'none'; // Ocultar si no hay selección
    }
}

function handleSubmit(event) {
    event.preventDefault(); // Evitar el envío del formulario
    alert("Gracias por tu mensaje, " + document.getElementById('name').value + "! Nos pondremos en contacto contigo pronto."); // Mensaje de agradecimiento
    // Aquí puedes agregar código para manejar el envío real del formulario si es necesario.
    document.getElementById('contact-form').reset(); // Limpiar el formulario
}

