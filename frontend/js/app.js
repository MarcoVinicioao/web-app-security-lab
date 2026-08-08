const form = document.getElementById("task-form");
const input = document.getElementById("task");
const taskList = document.getElementById("task-list");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const taskText = input.value;

    if (taskText === "") {
        return;
    }

    const response = await fetch("http://localhost:5000/api/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            task: taskText
        })
    });

    const data = await response.json();

    const newTask = document.createElement("li");

    newTask.textContent = data.task;

    taskList.appendChild(newTask);

    input.value = "";
});


async function loadTasks() {
    const response = await fetch("http://localhost:5000/api/tasks");

    const tasks = await response.json();

    taskList.innerHTML = "";

    tasks.forEach(function (task) {
        const newTask = document.createElement("li");

        newTask.textContent = task.task;

        taskList.appendChild(newTask);
    });
}

loadTasks();
