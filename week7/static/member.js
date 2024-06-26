window.addEventListener("load", () => {
    fetchAndDisplay(); 
});

function fetchAndDisplay() {
    fetch("/api/messages")
        .then(response => response.json())
        .then(data => {
            // display welcomeName
            const name = data.name;
            const welcomeName = document.getElementById("welcome-name");
            welcomeName.textContent = `${name}, 歡迎登入系統`;
            
            // classifyMessages and display
            const messages = data.messages;
            const currentUsername = data.current_username;
            const messageBoard = document.querySelector(".message-board");
            const classifiedMessages = classifyMessages(messages);
            const originalMessageGroups = Object.values(classifiedMessages);
            const sortedMessages = originalMessageGroups.flat().sort((a, b) => b.id - a.id);
            sortedMessages.forEach(message => {
                const messageComponent = createMessageComponent(message, currentUsername);
                messageBoard.appendChild(messageComponent);
            });
        });
}

  
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
      classified[name].push({ name: name, content: content, id: id, username: username });
    });
    return classified;
  }



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
const queryUsernameInput = document.getElementById("query-username-input");
const replyQueryUsername = document.getElementById("reply-query-username");

async function handleQueryUsernameFormSubmit(event) {
    event.preventDefault();
    replyQueryUsername.textContent = "";

    const query_username = queryUsernameInput.value.trim();
    const paragraphElement = document.createElement("p");
    const request_and_response = await fetch(`/api/member?username=${query_username}`);
    const data = await request_and_response.json();

    if (data.data !== null) {
        const { name, username } = data.data;
        const reply_content = `${name}(${username})`;
        paragraphElement.textContent = reply_content;
        replyQueryUsername.appendChild(paragraphElement);
    } else {
        paragraphElement.textContent = "無此會員";
        replyQueryUsername.appendChild(paragraphElement);
    }
    clearFormInputs();
}

queryUsernameForm.addEventListener("submit", handleQueryUsernameFormSubmit);


// rename feature
const updateUsernameForm = document.getElementById("update-username-form");
const updateUsernameInput = document.getElementById("update-username-input");
const replyUpdateUsername = document.getElementById("reply-update-username");

updateUsernameForm.addEventListener("submit", handleUpdateUsername);

async function handleUpdateUsername(event) {
    event.preventDefault();
    replyUpdateUsername.textContent = "";

    const newName = updateUsernameInput.value.trim();
    const response = await fetch("/api/member", {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: newName
        })
    });

    const data = await response.json();

    if (data.ok) {
        const paragraphElement = document.createElement("p");
        paragraphElement.textContent = "更新成功";
        replyUpdateUsername.appendChild(paragraphElement);
        updateWelcomeName(newName);
    } else {
        const paragraphElement = document.createElement("p");
        paragraphElement.textContent = "更新失敗";
        replyUpdateUsername.appendChild(paragraphElement);
    };
    clearFormInputs();
}

function updateWelcomeName(newName){
    const welcomeName = document.getElementById("welcome-name");
    welcomeName.textContent = `${newName}, 歡迎登入系統`;

}

function clearFormInputs(){
    queryUsernameInput.value = "";
    updateUsernameInput.value = "";
}

