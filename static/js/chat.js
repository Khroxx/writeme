let messageCounter = 0;



async function sendMessage(){
    let form = new FormData();
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let date = formatDate(new Date());
    let json = await fetchJson(form, token);
    messageCounter++;
    const messageId = `deleteMessage${messageCounter}`;
    await innerHTML(date, username.value, messageField.value, 'loading',  messageId)
    try {
        document.getElementById(messageId).remove();
        await innerHTML(date, json.fields.author, messageField.value, 'black', messageId)
    } catch (error) {
        document.getElementById(messageId).remove();
        await innerHTML(date, json.fields.author, messageField.value, 'red', messageId)
    }
    messageField.value = '';
}

async function fetchJson(form, token){
    form.append('textmessage', messageField.value);
    form.append('csrfmiddlewaretoken', token);
    let response = await fetch('/chat/', {
        method: 'POST',
        body: form
    })
    let json = await response.json();
    return json;
}

async function innerHTML(date, author, message, color, messageId){
    return messageContainer.innerHTML += `<div id="${messageId}" class="message-div">
    <span class="loading">[${date}]</span> <b>${author}</b>: <span class="${color}"> ${message}</span>
    </div>`;
}

function formatDate(date) {
    let day = date.getDate();
    let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    let month = months[date.getMonth()];
    let year = date.getFullYear();

    day = day < 10 ? '0' + day : day;        
    
    return month + ' ' + day + ', ' + year;
}