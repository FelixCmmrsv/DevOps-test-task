async function callApi(endpoint) {
    const idInstance = document.getElementById('idInstance').value;
    const ApiTokenInstance = document.getElementById('ApiTokenInstance').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const message = document.getElementById('message').value;
    const fileUrl = document.getElementById('fileUrl').value;

    let url = `/${endpoint}`;
    let payload = {
        idInstance,
        ApiTokenInstance
    };

    if (endpoint === 'sendMessage') {
        payload.phoneNumber = phoneNumber;
        payload.message = message;
    } else if (endpoint === 'sendFileByUrl') {
        payload.phoneNumber = phoneNumber;
        payload.fileUrl = fileUrl;
    }

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
    const data = await response.json();
    document.getElementById('responseOutput').textContent = JSON.stringify(data, null, 2);
}
