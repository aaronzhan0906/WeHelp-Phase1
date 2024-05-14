window.addEventListener("load", () => {
    fetch("/api/messages")
        .then(response => response.json())
        .then(data => {
            const messages = data.messages;
            const currentUsername = data.current_username;
            const messageBoard = document.querySelector(".message-board");
            // classifyMessages
            const classifiedMessages = classifyMessages(messages);

            const originalMessageGroups = Object.values(classifiedMessages);
            //arrangement in descending power
            const sortedMessages = originalMessageGroups.flat().sort((a, b) => b.id - a.id);
            // create message components
            sortedMessages.forEach(message => {
                const messageComponent = createMessageComponent(message, currentUsername);
                messageBoard.appendChild(messageComponent);
            });
        });
});


function classifyMessages(messages) {
    const classified = {};
    messages.forEach(message => {
        const id = message[0];
        const name = message[1];
        const content = message[2];
        const username = message[3];
        
        if (!classified[name]) {
            classified[name] = [];
        }
        classified[name].push({ name: name, content: content, id: id, username: username});
    });
    return classified;
};


function createMessageComponent(message, currentUsername) {
    const messageGroup = document.createElement("div");
    messageGroup.classList.add("message-group");

    const messageAuthor = document.createElement("p");
    messageAuthor.classList.add("message-author");
    messageAuthor.textContent = message.name;

    const messageColon = document.createElement("p");
    messageColon.classList.add("message-colon");
    messageColon.textContent = ":";

    const messageContent = document.createElement("p");
    messageContent.classList.add("message-content");
    messageContent.textContent = message.content;

    messageGroup.appendChild(messageAuthor);
    messageGroup.appendChild(messageColon);
    messageGroup.appendChild(messageContent);

    // If the message was written by the current user, add a delete button
    if (message.username === currentUsername) { 
        const deleteButton = document.createElement("button");
        deleteButton.classList.add("delete-button");
        deleteButton.textContent = "X";
        deleteButton.addEventListener("click", () => {
            const requestData = {
                message_id: message.id,
                current_username: currentUsername
            };

            fetch("/deleteMessage",{
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(requestData)
            })
            .then(response => {
                if(response.ok){
                    messageGroup.remove();
                }
            })
        });
        messageGroup.appendChild(deleteButton);
    }

    return messageGroup;
};


// query username feature
const queryUsernameForm = document.getElementById("query-username-form");
const queryUsernameInput = document.getElementById("query-username");
const replyQueryUsername = document.getElementById("reply-query-username")

queryUsernameForm.addEventListener("submit", async(event) => {
    event.preventDefault();
    replyQueryUsername.textContent=""

    const query_username = queryUsernameInput.value.trim();
    const paragraphElement = document.createElement("p");
    const response = await fetch(`/api/member?username=${query_username}`);
    const data = await response.json();

    if(data.data !== null ){
        const {name, username} = data.data;
        const reply_content = `${name}(${username})`;
        paragraphElement.textContent = reply_content;
        replyQueryUsername.appendChild(paragraphElement);

    } else {
       paragraphElement.textContent = "無此會員";
       replyQueryUsername.appendChild(paragraphElement)
    }
})


// rename feature