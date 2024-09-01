function loadClientTests(button) {
    const clientId = button.getAttribute('data-client-id');

    // Redirect to the route
    window.location.href = `/client/${clientId}/tests`;
}