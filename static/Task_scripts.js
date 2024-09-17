function loadJobTasks(button) {
    const test_id = button.getAttribute('data-test-id');
    const clientName = button.getAttribute('data-client-name');
    const client_id = button.getAttribute('data-client-id');
    const TestName = button.getAttribute('data-test-name');
    const jobName = button.getAttribute('data-job-name');
    const jobId = button.getAttribute('data-job-id');
    // /<string:clientName>/<int:client_id>/<string:TestName>/<int:test_id>/<string:jobName>/<int:job_id>/tasks
    // Redirect to the route
    //
    window.location.href = `/${clientName}/${client_id}/${TestName}/${test_id}/${jobName}/${jobId}/tasks`;
}

function submitFormTask(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form element
    const form = document.getElementById('createTaskForm');

    // Serialize the form data
    const formData = new FormData(form);
    var button = document.querySelector('button[data-job-id]');
    jobIdtoAddTask = button.getAttribute('data-job-id');
    //console.log(clientIdtoAddTest);
    //console.log(formData);

    // Send the POST request to the server
    fetch(`/createTaskInJob/${jobIdtoAddTask}`, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Close the modal
            var createModal = bootstrap.Modal.getInstance(document.getElementById('createTaskModal'));
            createModal.hide();

            // Show the toast notification
            //show the toast
              var deleteToast = new bootstrap.Toast(document.getElementById('crudToast'));
              // Update the toast body content
              document.querySelector('#crudToast .toast-body').textContent = 'task successfully added to database';
              deleteToast.show();

            // Optionally, reset the form if you need to use it again right after closing
            //form.reset();
            // Refresh the page
            setTimeout(() => {
                location.reload(true); // Refresh the page
            }, 1500); // Delay to show the toast before refreshing
        } else {
            // Display an error message inside the modal
            const responseDiv = document.getElementById('responseMessage');
            responseDiv.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const responseDiv = document.getElementById('responseMessage');
        responseDiv.innerHTML = '<div class="alert alert-danger">An error occurred while creating the task.</div>';
    });
}