function loadClientTests(button) {
    const clientId = button.getAttribute('data-client-id');
    const clientName = button.getAttribute('data-client-name');

    // Redirect to the route
    window.location.href = `/${clientName}/${clientId}/tests`;
}

function submitFormTest(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form element
    const form = document.getElementById('createTestForm');

    // Serialize the form data
    const formData = new FormData(form);
    var button = document.querySelector('button[data-test-id]');
    clientIdtoAddTest = button.getAttribute('data-test-id');
    console.log(clientIdtoAddTest);
    console.log(formData);

    // Send the POST request to the server
    fetch(`/createTestInClient/${clientIdtoAddTest}`, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Close the modal
            var createModal = bootstrap.Modal.getInstance(document.getElementById('createTestModal'));
            createModal.hide();

            // Show the toast notification
            //show the toast
              var deleteToast = new bootstrap.Toast(document.getElementById('crudToast'));
              // Update the toast body content
              document.querySelector('#crudToast .toast-body').textContent = 'test successfully added to database';
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
        responseDiv.innerHTML = '<div class="alert alert-danger">An error occurred while creating the test.</div>';
    });
}

//DELETE
function deleteTest(button) {
  // Store the client ID and the button element
  testIdToDelete = button.getAttribute('data-test-id');
  console.log(testIdToDelete);
  deleteButton = button;

  // Show the Bootstrap modal
  var deleteModal = new bootstrap.Modal(document.getElementById('deleteConfirmationModal'), {});
  deleteModal.show();
}

// Handle the confirmation click event
document.getElementById('confirmDelete').addEventListener('click', function() {
  // Proceed with the deletion
  fetch(`/delete-test/${testIdToDelete}`, {
      method: 'DELETE',
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .then(data => {
      if (data.status === 'success') {
          console.log('Delete successful:', data);
          console.log('Removing element:', deleteButton.closest('.card'));
          // Remove the client item from the DOM
          deleteButton.closest('.card').remove();
          console.log('Element removed:');
          //show the toast
          var deleteToast = new bootstrap.Toast(document.getElementById('crudToast'));
          // Update the toast body content
          document.querySelector('#crudToast .toast-body').textContent = 'test successfully deleted from database';
          deleteToast.show();
      } else {
          console.error('Server response error:', data.message);
          alert('Error: ' + data.message);
      }
  })
  .catch(error => {
      console.error('Fetch error:', error);
      alert('An error occurred while deleting the client.');
  });

    // Hide the modal after deletion
      var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteConfirmationModal'));
      deleteModal.hide();
});