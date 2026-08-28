
## Part 1: Concept

### What is an Event?
An **event** is a user's action on the webpage — clicking a button, typing in a box, moving the mouse, submitting a form, etc.

**React event handling basics:**
1. React uses **camelCase** naming: `onClick` (not `onclick`), `onChange`, `onSubmit`
2. You pass a **function** (not a string) as the handler: `onClick={handleClick}` — NOT `onClick="handleClick()"`
3. React uses **Synthetic Events** — a wrapper around browser events so behavior is consistent across browsers
4. To prevent default browser behavior: use `event.preventDefault()`

---

## Part 2: Basic Examples (Build these one by one)

### Example 1: Click Event
```jsx
import { useState } from "react";

function ClickCounter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}
export default ClickCounter;
```
**Explain:** `onClick={handleClick}` — we pass the function reference, no parentheses. Parentheses `handleClick()` would run immediately on render.

### Example 2: Inline Arrow Function (passing arguments)
```jsx
function Greeting() {
  const sayHello = (name) => {
    alert(`Hello, ${name}!`);
  };

  return (
    <div>
      {/* Arrow function needed when passing arguments */}
      <button onClick={() => sayHello("Ayesha")}>Greet Ayesha</button>
      <button onClick={() => sayHello("Ahmed")}>Greet Ahmed</button>
    </div>
  );
}
```

### Example 3: onChange — handling input
```jsx
import { useState } from "react";

function LiveInput() {
  const [text, setText] = useState("");

  function handleChange(event) {
    setText(event.target.value); // event.target = the input element
  }

  return (
    <div>
      <input type="text" onChange={handleChange} placeholder="Type something..." />
      <p>You typed: {text}</p>
    </div>
  );
}
```
**Explain:** `event.target.value` is how we read what the user typed. This is called a **controlled component** (input value controlled by state).

### Example 4: onSubmit with preventDefault
```jsx
import { useState } from "react";

function SimpleForm() {
  const [name, setName] = useState("");

  function handleSubmit(event) {
    event.preventDefault(); // stops page reload
    alert(`Form submitted with name: ${name}`);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```
**Explain:** Forms reload the page by default — `preventDefault()` stops that.

### Example 5: Mouse Events
```jsx
function HoverBox() {
  return (
    <div
      onMouseEnter={() => console.log("Mouse entered!")}
      onMouseLeave={() => console.log("Mouse left!")}
      onDoubleClick={() => alert("Double clicked!")}
      style={{ width: 200, height: 100, background: "lightblue", padding: 10 }}
    >
      Hover over me
    </div>
  );
}
```

---

## Part 3: End-to-End Project — Task Manager (To-Do App)

Uses: onClick, onChange, onSubmit, event object, preventDefault, conditional events.

```jsx
import { useState } from "react";

function TaskManager() {
  const [tasks, setTasks] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [filter, setFilter] = useState("all"); // all | active | done

  // Handle typing
  function handleInputChange(event) {
    setInputValue(event.target.value);
  }

  // Handle form submit (Add Task)
  function handleAddTask(event) {
    event.preventDefault();

    if (inputValue.trim() === "") {
      alert("Task cannot be empty!");
      return;
    }

    const newTask = {
      id: Date.now(),
      text: inputValue,
      isDone: false,
    };

    setTasks([...tasks, newTask]);   // add new task
    setInputValue("");               // clear input
  }

  // Handle Delete (uses id argument)
  function handleDelete(id) {
    const updated = tasks.filter((task) => task.id !== id);
    setTasks(updated);
  }

  // Handle Toggle complete
  function handleToggle(id) {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, isDone: !task.isDone } : task
      )
    );
  }

  // Filter logic
  const visibleTasks = tasks.filter((task) => {
    if (filter === "active") return !task.isDone;
    if (filter === "done") return task.isDone;
    return true;
  });

  return (
    <div style={{ maxWidth: 450, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>📝 Task Manager</h1>

      {/* Form: onSubmit event */}
      <form onSubmit={handleAddTask}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Enter a task..."
        />
        <button type="submit">Add Task</button>
      </form>

      {/* Filter buttons: onClick with arguments */}
      <div style={{ margin: "15px 0" }}>
        <button onClick={() => setFilter("all")}>All</button>
        <button onClick={() => setFilter("active")}>Active</button>
        <button onClick={() => setFilter("done")}>Completed</button>
      </div>

      {/* Task list */}
      <ul style={{ listStyle: "none", padding: 0 }}>
        {visibleTasks.map((task) => (
          <li
            key={task.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "8px",
              borderBottom: "1px solid #ddd",
              textDecoration: task.isDone ? "line-through" : "none",
            }}
          >
            <span onClick={() => handleToggle(task.id)} style={{ cursor: "pointer" }}>
              {task.text}
            </span>

            <button onClick={() => handleDelete(task.id)}>❌</button>
          </li>
        ))}
      </ul>

      <p>Total: {tasks.length} | Completed: {tasks.filter(t => t.isDone).length}</p>
    </div>
  );
}

export default TaskManager;
```

### Use in App.js:
```jsx
import TaskManager from "./TaskManager";

function App() {
  return <TaskManager />;
}
export default App;
```

---

