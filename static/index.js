const csvForm = document.querySelector("#csv-form");

/** @param {Event} event */
const handleSubmit = (event) => {
  event.preventDefault();

  const form = event.currentTarget;
    console.log(form)

  const file = document.querySelector('#csvUpload')
  console.log(file)

  const url = new URL(form.action);
  const formData = new FormData(form);

  console.log(formData)

  const fetchOptions = {
    method: form.method,
    body: formData,
  };

  console.log(fetchOptions);

  fetch(url, fetchOptions);
};

csvForm.addEventListener("submit", handleSubmit);
