async function submitTask() {

    const query = document.getElementById("query").value;
    const task = document.getElementById("task").value;

    if (query.trim() === "") {
        alert("Please enter a query.");
        return;
    }

    document.getElementById("loading").innerHTML = "⏳ Generating response...";
    document.getElementById("result").innerHTML = "";

    let endpoint = "";

    switch(task){

        case "qa":
            endpoint = "/qa/";
            break;

        case "explain":
            endpoint = "/explain/";
            break;

        case "quiz":
            endpoint = "/quiz/";
            break;

        case "summarize":
            endpoint = "/summarize/";
            break;

        case "learn":
            endpoint = "/learn/";
            break;
    }

    let body = {
        query: query
    };

    if(task === "quiz"){
        body.number_of_questions = 5;
    }

    try{

        const response = await fetch(endpoint,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(body)
        });

        const data = await response.json();

        document.getElementById("loading").innerHTML = "";

        if(data.success){

           document.getElementById("result").innerHTML = `
<h2 style="color:#2563eb">${data.task}</h2>

<hr style="margin:15px 0">

<div class="answer">

${data.output.replace(/\n/g,"<br>")}

</div>
`;

        }else{

            document.getElementById("result").innerHTML =
            "<p>Something went wrong.</p>";

        }

    }catch(error){

        document.getElementById("loading").innerHTML = "";

        document.getElementById("result").innerHTML =
        "<p>Server Error</p>";

        console.log(error);
    }

}