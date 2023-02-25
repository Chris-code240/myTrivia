
const start = document.getElementById('start')


start.addEventListener('click',(ev)=>{

    ev.preventDefault()
    
    const board = document.getElementById('question-board')
    const type = document.getElementById('type')
    const score = document.getElementById('score')
    const time_wrapper = document.getElementById('time-wrapper')
    const time_ele = document.getElementById('time')

    let questions = null
    let already_viewd_questions = []

    const controller = new AbortController()
    const signal = controller.signal
    let get_question = ()=>{
    
        Array.from(board.children).forEach(ele=>{ele.remove()})
    
        fetch('/questions/'+type.textContent,{
    
            signal:signal,
            headers:{"Content-type":"application/json"},
            method:"POST",
            body:JSON.stringify(already_viewd_questions)
        }).then((res)=>{return res.json()}).then((jsonResponse)=>{
            // alert(jsonResponse['answers'])
            if(jsonResponse["success"] == false){
                controller.abort()
            }else{
                already_viewd_questions.push(jsonResponse['id'])
                console.log(already_viewd_questions)
                let p = document.createElement('p')
                p.setAttribute('class','text-2xl')
                p.textContent = jsonResponse['question']
                board.appendChild(p)
    
    
                let div = document.createElement('div')
                div.setAttribute('class','answers space-x-1 my-3 text-2xl')
    
                let answers = JSON.parse(jsonResponse['answers'])
                for(let answer in answers){
                    let a = document.createElement('a')
                    a.setAttribute('class','p-1 px-6 py-1 rounded-full hover:bg-purple')
                    a.textContent = answer
                    div.appendChild(a)
    
                    a.addEventListener('click',(e)=>{
                        e.preventDefault()
                        if(a.textContent == jsonResponse['correct_answer']){
                            score.textContent = Number(score.textContent) + 1
                            a.style.backgroundColor = 'green'
                        }else{
                            a.style.backgroundColor = 'red'
                        }
                        setTimeout(() => {
                            get_question()
                        }, 500);
                    })
                }
    
                board.appendChild(div)
            }
        })
    
    }

let game_over = ()=>{
    let over_text = document.createElement('p')
    over_text.setAttribute('class','text-4xl')
    over_text.textContent = 'Game Over!'
    Array.from(board.children).forEach(ele=>{ele.remove()})
    board.appendChild(over_text)
    start.textContent = 'Play Again'
    start.classList.remove('hidden')
    clearInterval(time_stopper)


}

signal.addEventListener('abort',game_over)

    time_ele.textContent = 0
    score.textContent = 0
    Array.from(board.children).forEach(ele=>{ele.remove()})

    board.classList.remove('hidden')
    score.classList.remove('hidden')
    time_wrapper.classList.remove('hidden')
    start.classList.add('hidden')
    if(signal.aborted != true){
        get_question()
    }

    let time_stopper = setInterval(() => {
        time_ele.textContent = Number(time_ele.textContent) + 1
        if(Number(time_ele.textContent)  == 10){
            controller.abort()
            clearInterval(time_stopper)
        }

    }, 1000);


})







