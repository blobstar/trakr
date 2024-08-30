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
            form.action = `/update-client/${clientId}`;
            console.log("Form action URL set to:", form.action);
            // #updateClientModal is in update_client.py and #client-name is in forms.py
            document.querySelector('#updateClientModal #clientName').value = data.client || '';
        } else {
            alert("Error retrieving client item");
        }
    })
    .catch(error => console.error('Error4:', error));

}
function updateClient(clientId) {
    console.log("js working");

    var clientId = clientId.getAttribute('data-client-id');


    fetch(`/update-client/${clientId}`, {
        method: 'PUT',  // Changed to PUT
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'refID': clientId
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status === 'success') {
            alert("Item updated successfully");
        } else {
            alert("Error updating item");
        }
    })
    .catch(error => console.error('Error:', error));
}