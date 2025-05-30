const todo = document.querySelector(`#todo`)
const doing = document.querySelector(`#doing`)
const done = document.querySelector(`#done`)


function noteFunctionAdder(note) {

    note.addEventListener("blur", () => {
        fetch("/update_note", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                id: note.getAttribute("data-id"),
                body: note.value
            })
        })
    })

    note.addEventListener("dragstart", (event) => {
        event.dataTransfer.setData("text/plain", note.getAttribute("data-id"))
    })
}

function columnEvents() {
    [todo, doing, done].forEach(column => {
        column.addEventListener("dragover", (event) => {
            event.preventDefault()
        })

        column.addEventListener("drop", (event) => {
            event.preventDefault()

            const noteId = event.dataTransfer.getData("text/plain")
            const note = document.querySelector(`[data-id='${noteId}']`)
            column.appendChild(note)

            fetch("/update_column", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    id: noteId,
                    column: column.id
                })
            })
        })
    })
}




function addNote(column) {

    const newNote = document.createElement("textarea")
    newNote.setAttribute("draggable", true)
    newNote.classList.add("note")

    if (column === "todo") {
        todo.appendChild(newNote)
    }
    else if (column === "doing") {
        doing.appendChild(newNote)
    }
    else if (column === "done") {
        done.appendChild(newNote)
    }

    fetch("/add_note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            body: newNote.value,
            column: column
        })
    })
        .then(response => response.json())
        .then(data => {
            newNote.setAttribute("data-id", data.id)
            noteFunctionAdder(newNote)
        })    
}

document.querySelectorAll("textarea.note").forEach(noteFunctionAdder);

columnEvents()