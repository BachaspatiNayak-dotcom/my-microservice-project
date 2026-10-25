document.getElementById("emplink").addEventListener("click",function(event){

    event.preventDefault(); //do not navigate anywhere,run javascript and call fastapi

    fetch("http://127.0.0.1:8000/emp_details/")  //used to make http requests
    .then(response=>response.json())            //turning fastapi json response to a array of objects
    .then(
        data=>{
            console.log(data);
            data.forEach(emp=> {
                document.getElementById("empTableBody").innerHTML+=`
                <tr>
                    <td>${emp.eid}</td>
                    <td>${emp.ename}</td>
                    <td>${emp.sal}</td>
                    <td>${emp.deptno}</td>
                </tr>
                `;
            });
        })

});

document.getElementById("dept").addEventListener("click",function(event){

    event.preventDefault()

    fetch("http://127.0.0.1:8000/dept_details")
    .then(response=>response.json())
    .then(
        data=>{
            console.log(data)
            data.forEach(
                dept=>{
                    document.getElementById("deptTableBody").innerHTML+=`
                    <tr>
                    <td>${dept.ID}</td>
                    <td>${dept.dname}</td>
                    </tr>
                    `
                }
            )
        }
    )
})