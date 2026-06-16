const loadBtn=document.getElementById("loadBtn");
const usersContainer=document.getElementById("usersContainer");
const loading=document.getElementById("loading");



loadBtn.addEventListener("click",getUsers);


async function getUsers(){
  loading.innerHTML="Loading...";
  const response=await fetch("https://jsonplaceholder.typicode.com/users");
  const data=await response.json();
  console.log(data)
  
  data.forEach(user=>{
    usersContainer.innerHTML+=`
      <div class="card">
      <h1>${user.name}</h1>
      <p>${user.email}</p>
      <p>${user.phone}</p>
      <p>

      </div>
    `;
  })
}