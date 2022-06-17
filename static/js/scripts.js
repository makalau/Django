function mudaFoto(foto){
	document.getElementById("icone").src = foto;
}

function buscar(id){
	window.document.location.replace(`/editar/${id}`);
}

function deletar(id){
	cont = window.confirm("Tem certeza que deseja deletar o registro do banco de dados?:")
	if(cont){
		window.document.location.replace(`/deletar/${id}`);
	}
}

function msg(){
	nome = window.document.getElementsByName("nome")[0].value;
	telefone = window.document.getElementsByName("telefone")[0].value;
	email = window.document.getElementsByName("email")[0].value

	if (nome && telefone && email){
		if (email.indexOf("@") != -1){
			window.alert("Usuário cadastrado com sucesso!");
		}
	}
	else if(nome && telefone && email == false){
		window.alert("Usuário cadastrado com sucesso!");
	}

	else{
		window.alert("[ATENÇÃO] Preencha os campos solicitados.")
	}
}