// 创建消息组件
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

  if (message.username === currentUsername) { 
    const deleteButton = document.createElement("button");
    deleteButton.classList.add("delete-button");
    deleteButton.textContent = "X";
    deleteButton.addEventListener("click", () => {
      console.log("Delete button clicked for message:", message);
    });
    messageGroup.appendChild(deleteButton);
  }
  
  return messageGroup;
}

window.addEventListener("load", () => {
  fetch("/api/messages")
    .then(response => response.json()) 
    .then(data => {
      const messages = data.messages;
      const currentUsername = data.current_username;
      const messageBoard = document.querySelector(".message-board");
      console.log(messages, currentUsername);
      if (messageBoard) {
        messages.forEach(message => {
          const messageComponent = createMessageComponent(message, currentUsername);
          messageBoard.appendChild(messageComponent);
        });
      } 
    });
  });