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