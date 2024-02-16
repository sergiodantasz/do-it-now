function setDisplayNone(element) {
  element.style.display = 'none'
}

function isDisplayNone(element) {
  return element.style.display === 'none'
}

function setMessagesTimeOut() {
  const messagesContainer = document.querySelector('.messages')
  setTimeout(() => {
    if (!isDisplayNone(messagesContainer)) setDisplayNone(messagesContainer)
  }, 5000)
  const messages = messagesContainer.querySelectorAll('.message')
  let shownMessages = messages.length
  messages.forEach((message) => {
    const closeIcon = message.querySelector('.close-icon')
    closeIcon.addEventListener('click', () => {
      setDisplayNone(message)
      shownMessages--
      if (shownMessages === 0 && !isDisplayNone(messagesContainer)) setDisplayNone(messagesContainer)
    })
  })
}

document.addEventListener('DOMContentLoaded', setMessagesTimeOut)
