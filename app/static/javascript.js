(function(win,doc){
    'use strict';

    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo deletar o registro ?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    //Ajax do form
    if (doc.querySelector('#form')) {
  let form = doc.querySelector('#form')
  function sendForm(event) {
    event.preventDefault();
    let data = new FormData(form);
    let ajax = new XMLHttpRequest();
    let token = doc.querySelectorAll('input')[0].value;
    ajax.open('POST', form.action);
    ajax.setRequestHeader('X-CSRF-TOKEN', token);
    ajax.onreadystatechange = function () {
      if (ajax.readyState === 4) {
        if (ajax.status === 200) {
          let response = JSON.parse(ajax.responseText);
          if (response.status === 'success') {
            let result = doc.querySelector('#result');
            result.innerHTML = 'Cadastro realizado com sucesso';
            result.classList.add('alert');
            result.classList.add('alert-success');
          } else if (response.status === 'error') {
            let result = doc.querySelector('#result');
            result.innerHTML = response.message;
            result.classList.add('alert');
            result.classList.add('alert-danger');
          }
        } else {
          let result = doc.querySelector('#result');
          result.innerHTML = 'Ocorreu um erro ao enviar o formulário. Por favor, tente novamente mais tarde.';
          result.classList.add('alert');
          result.classList.add('alert-danger');
        }
      }
    };
    ajax.send(data);
    form.reset();
  }
  form.addEventListener('submit', sendForm, false);
}



})(window,document);