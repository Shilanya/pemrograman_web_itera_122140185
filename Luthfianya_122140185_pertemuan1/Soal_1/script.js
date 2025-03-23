document.addEventListener("DOMContentLoaded", loadTasks);

function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();
    if (taskText === "") return;

    let li = document.createElement("li");
    li.textContent = taskText;
    li.onclick = () => toggleComplete(li);
    
    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Hapus";
    deleteBtn.onclick = (e) => {
        e.stopPropagation();
        deleteTask(li);
    };
    
    li.appendChild(deleteBtn);
    document.getElementById("taskList").appendChild(li);
    
    saveTasks();
    taskInput.value = "";
}

function toggleComplete(li) {
    li.classList.toggle("completed");
    saveTasks();
}

function deleteTask(li) {
    li.remove();
    saveTasks();
}

function saveTasks() {
    let tasks = [];
    document.querySelectorAll("#taskList li").forEach(li => {
        tasks.push({ text: li.childNodes[0].nodeValue, completed: li.classList.contains("completed") });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    let taskList = document.getElementById("taskList");
    taskList.innerHTML = "";
    tasks.forEach(task => {
        let li = document.createElement("li");
        li.textContent = task.text;
        if (task.completed) li.classList.add("completed");
        li.onclick = () => toggleComplete(li);
        
        let deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Hapus";
        deleteBtn.onclick = (e) => {
            e.stopPropagation();
            deleteTask(li);
        };
        
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    });
}
