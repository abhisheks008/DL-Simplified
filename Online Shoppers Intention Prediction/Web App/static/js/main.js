document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.prediction-form');
    if (!form) {
        return;
    }

    form.addEventListener('submit', function (event) {
        const fields = form.querySelectorAll('input[type="number"], select');
        let valid = true;

        fields.forEach((field) => {
            if (!field.checkValidity()) {
                valid = false;
                const message = field.dataset.invalidMessage || 'Please enter a valid value.';
                let error = field.parentNode.querySelector('.field-error');
                if (!error) {
                    error = document.createElement('span');
                    error.className = 'field-error';
                    field.parentNode.appendChild(error);
                }
                error.textContent = message;
            } else {
                const error = field.parentNode.querySelector('.field-error');
                if (error) {
                    error.textContent = '';
                }
            }
        });

        if (!valid) {
            event.preventDefault();
        }
    });
});
