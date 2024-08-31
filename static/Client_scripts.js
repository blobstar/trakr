function submitForm(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form element
    const form = document.getElementById('createItemForm');

    // Serialize the form data
    const formData = new FormData(form);

    // Send the POST request to the server
    fetch('/items', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Close the modal
            var createModal = bootstrap.Modal.getInstance(document.getElementById('createItemModal'));
            createModal.hide();

            // Show the toast notification
            //show the toast
              var deleteToast = new bootstrap.Toast(document.getElementById('crudToast'));
              // Update the toast body content
              document.querySelector('#crudToast .toast-body').textContent = 'client successfully added to database';
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
        responseDiv.innerHTML = '<div class="alert alert-danger">An error occurred while creating the item.</div>';
    });
}
function deleteClient(button) {
  // Store the client ID and the button element
  clientIdToDelete = button.getAttribute('data-client-id');
  deleteButton = button;

  // Show the Bootstrap modal
  var deleteModal = new bootstrap.Modal(document.getElementById('deleteConfirmationModal'), {});
  deleteModal.show();
}

// Handle the confirmation click event
document.getElementById('confirmDelete').addEventListener('click', function() {
  // Proceed with the deletion
  fetch(`/delete-client/${clientIdToDelete}`, {
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
          document.querySelector('#crudToast .toast-body').textContent = 'client successfully deleted from database';
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

function loadUpdateForm(clientId) {
    var clientId = clientId.getAttribute('data-client-id');
    console.log(clientId)
    // Redirect to the route that renders the form with initial data
    fetch(`/get-client/${clientId}`, {
        method: 'GET',  // Use GET for retrieving data
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status === 'success') {
            new bootstrap.Modal(document.querySelector("#updateClientModal")).show();
            // Set client ID in the hidden field
            document.querySelector('#clientId').value = clientId;
            const form = document.querySelector('#updateItemForm');

            console.log("Form action URL set to:", form.action);
            // #updateClientModal is in update_client.py and #client-name is in forms.py
            document.querySelector('#updateClientModal #clientName').value = data.client || '';
            document.querySelector('#updateItemForm').setAttribute('onsubmit', `submitUpdateClientForm(${clientId}); return false;`);
        } else {
            alert("Error retrieving client item");
        }
    })
    .catch(error => console.error('Error:', error));
    }




function submitUpdateClientForm(clientId) {
    // Prepare the data from the form
    const form = document.querySelector('#updateItemForm');
    const formData = new FormData(form);

    // Perform the AJAX request to update the client
    fetch(`/update-client/${clientId}`, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status === 'success') {
            // Close the modal
            const modal = bootstrap.Modal.getInstance(document.querySelector("#updateClientModal"));
            modal.hide();

            // Show the toast
            const deleteToast = new bootstrap.Toast(document.getElementById('crudToast'));
            // Update the toast body content
            document.querySelector('#crudToast .toast-body').textContent = 'Client successfully added to database';
            deleteToast.show();

            // Optionally, reset the form if you need to use it again right after closing
            // form.reset();

            // Increase the delay before the page refreshes to give the toast time to be visible
            setTimeout(() => {
                location.reload(true); // Refresh the page
            }, 1500); // 3-second delay
        } else {
            // Handle any errors
            console.error('Update failed', data);
        }
    })
    .catch(error => console.error('Error:', error));
}

