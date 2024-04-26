function addProject() {
    let title = document.getElementById('title').value
    let link = document.getElementById('link').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'title': title,
                             'link': link})
    })
}

function clearProjects() {
           if (confirm("Вы уверены, что хотите удалить все проекты?")) {
               fetch('/clear', { method: 'GET' })
               .then(response => {
                   if (response.status === 204) {
                       location.reload();
                   }
               });
           }
       }