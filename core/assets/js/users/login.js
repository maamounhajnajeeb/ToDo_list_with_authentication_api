document.addEventListener('DOMContentLoaded', function(){
    const csrfToken = document.cookie
    .split("; ")
    .find(cookie=> cookie.startsWith("csrftoken"))
    .split("=")[1];
    const url = 'http://127.0.0.1:8000/api/v1/users/login/';
    const data = {
        username: 'MobasherHarmoush',
        password: '17AiGz48rhe'
    };
    fetch(url,
        {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrfToken
        },
        body: JSON.stringify(data)   
    })
    .then((response)=>{
        console.log(response)
    })
});
