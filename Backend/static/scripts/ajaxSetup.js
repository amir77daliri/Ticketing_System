function getCsrf() {
    let cookies = document.cookie.split(';')
    let csrf
    for(let i=0;i<cookies.length;i++){
        let key = cookies[i].split('=')
        if(key[0] === ' csrftoken' || key[0]=== 'csrftoken'){
            csrf = key[1]
            return csrf
        }
    }
}
function  csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup(
    {
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCsrf());
            }
        }
    }
)