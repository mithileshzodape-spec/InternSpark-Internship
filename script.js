// Selecting DOM Elements
const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');
const totalCount = document.getElementById('totalCount');
const clearAllBtn = document.getElementById('clearAllBtn');

// Local storage array or empty array
let tasksArr = JSON.parse(localStorage.getItem('myTasks')) || [];

// Initial Rendering
renderTasks();

// Function to render all tasks from array
function renderTasks() {
    taskList.innerHTML = '';
    
    tasksArr.forEach((task, index) => {
        const li = document.createElement('li');
        if (task.completed) {
            li.classList.add('completed');
        }

        li.innerHTML = `
            <span class="task-text" onclick="toggleTask(${index})">${task.text}</span>
            <button class="delete-btn" onclick="deleteTask(${index})">Delete</button>
        `;
        taskList.appendChild(li);
    });

    // Update Counter
    totalCount.textContent = tasksArr.length;
    
    // Save to LocalStorage
    localStorage.setItem('myTasks', JSON.stringify(tasksArr));
}

// Function to add new task
function addTask() {
    const textValue = taskInput.value.trim();
    
    if (textValue === '') {
        alert('Please enter a valid task!');
        return;
    }

    // Add new task object to list
    tasksArr.push({
        text: textValue,
        completed: false
    });

    taskInput.value = '';
    renderTasks();
}

// Toggle Complete status
function toggleTask(index) {
    tasksArr[index].completed = !tasksArr[index].completed;
    renderTasks();
}

// Delete single task
function deleteTask(index) {
    tasksArr.splice(index, 1);
    renderTasks();
}

// Clear All tasks
clearAllBtn.addEventListener('click', function() {
    if (tasksArr.length === 0) return;
    
    if (confirm('Are you sure you want to delete all tasks?')) {
        tasksArr = [];
        renderTasks();
    }
});

// Event Listener for button and Enter key
addBtn.addEventListener('click', addTask);

taskInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});