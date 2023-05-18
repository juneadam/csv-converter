const csvForm = document.querySelector('csv-form');
csvForm.addEventListener('submit', handleSubmit);

// /** @param {Event} event */
const handleSubmit = (event) => {
    event.preventDefault();

    const form = event.currentTarget
    const url = new URL(form.action)
    const fetchOptions = {
        method: form.method,
        body: FormData,
    }

    fetch(url, fetchOptions)
}