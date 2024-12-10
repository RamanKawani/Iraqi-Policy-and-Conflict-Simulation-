document.getElementById('simulation-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Collect data from form fields (use document.getElementById to get the values)
    let data = {
        government_type: 'Federal',
        economic_state: 'Developing',
        foreign_relations: 'Neutral'
    };

    fetch('/policy/simulate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Display results in the DOM
        document.getElementById('simulation-result').innerText = JSON.stringify(result, null, 2);
    });
});
