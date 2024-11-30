// Form Validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.needs-validation');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Phone number validation
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            const value = e.target.value.replace(/\D/g, '');
            if (value.length < 10 || value.length > 15) {
                input.setCustomValidity('رقم الهاتف يجب أن يكون بين 10 و 15 رقم');
            } else {
                input.setCustomValidity('');
            }
        });
    });
});

// Delete Confirmation
function confirmDelete(event, itemName) {
    if (!confirm(`هل أنت متأكد من حذف "${itemName}"؟`)) {
        event.preventDefault();
    }
}

// Auto-dismiss alerts
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade');
            setTimeout(() => alert.remove(), 150);
        }, 3000);
    });
});

// Add fade-in animation to cards
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => card.classList.add('fade-in'));
});
